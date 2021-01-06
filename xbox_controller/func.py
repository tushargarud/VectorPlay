import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
from anki_vector.util import degrees
from colorama import Fore, Back, Style, init

def smack(robot):
    print("SMASHING\n")
    robot.behavior.set_lift_height(1, 0, 0, 0, 0)
    robot.behavior.set_lift_height(0, 0, 0, 0, 0)

def lift(dire, robot):
    print(f"MOVING LIFT {dire}\n")
    if dire == "UP":
        robot.motors.set_lift_motor(2.0)
    elif dire == "DOWN":
        robot.motors.set_lift_motor(-.0)
    else:
        print(f"[lift] ERR, {dire} IS NOT A VALID DIRECTION\n\n")

def pprint(msg, robot):
    robot.say_text(msg)

def move_head(robot):
    hangl = robot.head_angle_rad
    if hangl <= 0.5:
        robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    else:
        robot.behavior.set_head_angle(MIN_HEAD_ANGLE)

def drive(dire, robot):
    if dire > 0:
        print("MOVING FORWARD\n")
        robot.motors.set_wheel_motors(dire/20, dire/20)
    elif dire < 0:
        print("MOVING BACKWARDS\n")
        robot.motors.set_wheel_motors(dire/22, dire/22)
    else:
        print("That's weird, you have a zero value")
    
def turn(dire, robot):
    if dire > 0:
        print("TURNING RIGHT\n")
        robot.motors.set_wheel_motors(dire/20, -dire/20)
    elif dire < 0:
        print("TURNING LEFT\n")
        robot.motors.set_wheel_motors(dire/20, -dire/20)
    else:
        print(Back.RED + "That's weird, you have a zero value")