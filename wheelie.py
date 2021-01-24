import anki_vector
from anki_vector.util import distance_mm

with anki_vector.Robot() as robot:
    robot.world.connect_cube()

    if robot.world.connected_light_cube:
        robot.behavior.pop_a_wheelie(robot.world.connected_light_cube)
