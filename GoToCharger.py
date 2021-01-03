#!/usr/bin/env python3

import anki_vector

with anki_vector.Robot() as robot:
    robot.behavior.drive_on_charger()
