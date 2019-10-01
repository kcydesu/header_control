# header_control
Library to set and maintain a certain header for a servo motor

RPi.GPIO comes with Raspbian

In RPi terminal
```
cd ~
git clone https://github.com/kcydesu/servo-pi.git
cd servo-pi
sudo pip install -e .
```
```
cd ~
git clone https://github.com/adafruit/Adafruit_Python_BNO055.git
cd Adafruit_Python_BNO055
sudo pip install -e .
```
```
cd ~
git clone https://github.com/kcydesu/header_control.git
cd header_control
sudo pip install -e .
```

For the physical connection, you will need the Adafruit BNO055, and a servo motor.  We used the Tower Pro MicroServo 9g SG90.
To keep the BNO055 attached to the servo, we used common household supplies.  

In the picture below, we used index cards taped around the servo 'arms' with an index card formed into a holder for the BNO055.  That holder was then taped ontop of the index cards surrounding the servo arms.

![Physical Setup 1](https://github.com/NoelleTemple/header_control/blob/patch-2/pictures/20191001_103457.jpg)
![Physical Setup 2](https://github.com/NoelleTemple/header_control/blob/patch-2/pictures/20191001_103504.jpg)

The two pictures below show the pinout for the servo, and the RPi.  The BNO055 has the pinout labeled on the device for ease.
```
BNO055 pin 1 -> RPi pin 1 
BNO055 pin 2 -> RPi pin 9
BNO055 pin 3 -> RPi pin 5
BNO055 pin 4 -> RPi pin 3

Servo Vin -> RPi pin 17
Servo Gnd -> RPi pin 39
Servo Cntl -> RPi pin 18
```

Note that in the sample code this line can change the Servo Cntl pin:
```
servo_pin = 18
```
This value is the board pin, NOT the GPIO number.

![RPi Pinout](https://github.com/NoelleTemple/header_control/blob/patch-2/pictures/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated.png)
![Servo Pinout](https://github.com/NoelleTemple/header_control/blob/patch-2/pictures/Servo-Motor-Wires.png)

The header_control package allows a user to input a desired heading value, and the servo will move to that point.  

Technically, there are 8 different scenarios that the servo could face; this code addresses all 8, making sure to notify the user when the desired heading is out of the servo's range, and adjusting automatically to fulfill the remaining scenarios.

To edit the desired heading value:

```
cd ~/header_control/test/
nano test.py
```

The line to change is:
```
goal = 60
```

To use the sample, make sure your physical setup is the same as the one described above and then use these lines in the terminal to execute.

```
cd ~/header_control/test/
python test.py
```

