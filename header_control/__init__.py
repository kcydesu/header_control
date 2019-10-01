from servo_pi.servo import Servo
from Adafruit_BNO055 import BNO055
import time


class HeaderControl:
    def __init__(self, servo_pin=18, bno055_i2c_address=0x29):
        self._servo = Servo(servo_pin)
        self._pos = 90
        self._servo.set_position(self._pos)
        print("Connected to servo on board pin {}".format(servo_pin))

        self._bno = BNO055.BNO055(address=bno055_i2c_address)

        if not self._bno.begin():
            raise RuntimeError('Failed to initialize BNO055!  Is the sensor connected?')

        status, self_test, error = self._bno.get_system_status()
        print('System status: {0}'.format(status))
        print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))

        if status == 0x01:
            print('System error: {0}'.format(error))
            print('See datasheet section 4.3.59 for the meaning.')
        if status == 0x0F:
            print('System is ready for commands, waiting for input.')

    def set_goal_heading(self, goal):
        self._head_goal = goal

    def maintain_goal(self):

        while True:
            cur_heading, _, _ = self._bno.read_euler()
            minval = abs((cur_heading - self._pos) % 360)
            maxval = abs((cur_heading + (180 - self._pos)) % 360)

            if minval < maxval:
                mode = 0x00
            else:
                mode = 0x01

            if ((cur_heading - 15) < self._head_goal) & ((cur_heading + 15) > self._head_goal):
                self._pos = self._pos
                print("Goal heading has been found and is being maintained.")
            elif mode == 0x00:
                if (self._head_goal > maxval) or (self._head_goal < minval):
                    print("Goal is out of range of servo.")
                elif self._head_goal < cur_heading:
                    self._pos -= 10
                    print("Finding... Current heading: {} Goal heading: {}".format(cur_heading,self._head_goal))
                elif self._head_goal > cur_heading:
                    self._pos += 10
                    print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
            else:
                if (self._head_goal > maxval) and (self._head_goal < minval):
                    print("Goal is out of range of servo.")
                elif (self._head_goal < maxval) & (cur_heading < maxval):
                    if self._head_goal < cur_heading:
                        self._pos -= 10
                        print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
                    elif self._head_goal > cur_heading:
                        self._pos += 10
                        print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
                elif (self._head_goal > minval) & (cur_heading > minval):
                    if self._head_goal < cur_heading:
                        self._pos -= 10
                        print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
                    elif self._head_goal > cur_heading:
                        self._pos += 10
                        print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
                elif (self._head_goal < maxval) & (cur_heading > maxval):
                    self._pos += 10
                    print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
                elif (self._head_goal > minval) & (cur_heading < minval):
                    self._pos -= 10
                    print("Finding... Current heading: {} Goal heading: {}".format(cur_heading, self._head_goal))
                else:
                    pass

            self._servo.set_position(self._pos)
            time.sleep(0.1)
