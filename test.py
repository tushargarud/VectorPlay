import anki_vector
import time

args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
    # robot.behavior.set_lift_height(1.0)
    robot.motors.set_wheel_motors(1000, 1000)
    time.sleep(5.0)