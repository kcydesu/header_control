from header_control import HeaderControl


def main():

    servo_pin = 18
    i2c_address = 0x29

    hc = HeaderControl(18,0x29)

    hc.set_goal_heading(65)
    hc.maintain_goal()


if __name__ =="__main__":
    main()