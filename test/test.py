from header_control import HeaderControl


def main():

    goal = 60
    servo_pin = 35
    i2c_address = 0x29

    hc = HeaderControl(servo_pin,i2c_address)

    hc.set_goal_heading(goal)
    hc.maintain_goal()


if __name__ =="__main__":
    main()
