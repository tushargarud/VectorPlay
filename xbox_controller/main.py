import inputs
import anki_vector
from inputs import get_gamepad
from anki_vector.util import degrees, distance_mm, speed_mmps
import time
import func
from colorama import Fore, Back, Style, init

def main():
    args = anki_vector.util.parse_command_args()
    loop = True
    with anki_vector.Robot(args.serial) as robot:
        # func.pprint("Starting manual control", robot)
        robot.behavior.drive_off_charger()
        print(Fore.GREEN + "BEGINNING LOOP STAGE\n-----------------------------------\n\n")
        print(Style.RESET_ALL)
        while loop == True:
            for event in get_gamepad():
                if event.code == "BTN_SOUTH" and event.state == 1: # A Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    func.smack(robot)

                if event.code == "ABS_HAT0Y": # DPAD
                    print("[inputs]", event.ev_type, event.code, event.state)
                    if event.state == -1: # UP
                        func.lift("UP", robot)
                    elif event.state == 1: # DOWN
                        func.lift("DOWN", robot)
                    else:
                        robot.motors.set_lift_motor(0)

                if event.code == "BTN_TR" and event.state == 1: # Right Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("FINDING CHARGER\n")
                    func.pprint("FINDING CHARGER", robot)
                    robot.behavior.drive_on_charger()

                if event.code == "BTN_EAST" and event.state == 1: # B Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("MOVING HEAD\n")
                    func.move_head(robot)

                if event.code == "ABS_Y":
                    if event.state >= 3000 or event.state <= -3000: # drive
                        print("[inputs]", event.ev_type, event.code, event.state)
                        func.drive(event.state, robot)
                    else:
                        robot.motors.set_wheel_motors(0, 0)

                if event.code == "ABS_RX": # Turn
                    if event.state >= 3000 or event.state <= -3000:
                        print("[inputs]", event.ev_type, event.code, event.state)
                        func.turn(event.state, robot)
                    else:
                        robot.motors.set_wheel_motors(0, 0)

                if event.code == "BTN_START" and event.state == 1: # Kill cmd
                    print("[inputs]", event.code, event.state)
                    print(Fore.RED + "KILLING LOOP, BYEBYE!!")
                    loop = False

if __name__ == "__main__":
    init()
    main()
