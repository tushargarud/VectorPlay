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

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""

import anki_vector
import argparse
import random

curse_words = ["Aai ghalia", "aai zawadyaa", "Behenchaoad", "Chuteya"]
random.shuffle(curse_words)

parser = argparse.ArgumentParser()
parser.add_argument("person_name")
args = anki_vector.util.parse_command_args(parser)

with anki_vector.Robot(args.serial) as robot: 
    robot.anim.play_animation('anim_movement_forward_01')
    robot.anim.play_animation('anim_eyepose_furious')
    robot.behavior.say_text(f"Ae {curse_words[0]} {args.person_name}")
    robot.behavior.say_text(curse_words[1])
    robot.behavior.say_text(curse_words[2])
    robot.behavior.say_text(curse_words[3])
    robot.anim.play_animation('anim_fistbump_success_03')
