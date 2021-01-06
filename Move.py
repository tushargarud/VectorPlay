#!/home/pi/virtual_envs/vector_venv/bin/python

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import anki_vector
import argparse
import time
from anki_vector.util import degrees, distance_mm, speed_mmps

parser = argparse.ArgumentParser()
parser.add_argument("direction")
args = anki_vector.util.parse_command_args(parser)

with anki_vector.Robot(args.serial) as robot:
    if args.person_name.lower() == 'forward':
        robot.behavior.drive_straight(distance_mm(50), speed_mmps(100), True)
    elif args.person_name.lower() == 'backward':
        robot.behavior.drive_straight(distance_mm(50)*-1, speed_mmps(100), True)
    elif args.person_name.lower() == 'left':
        robot.behavior.turn_in_place(degrees(90))
    elif args.person_name.lower() == 'right':
        robot.behavior.turn_in_place(degrees(-90))
    else:
        robot.motors.stop_all_motors()

    time.sleep(5)
