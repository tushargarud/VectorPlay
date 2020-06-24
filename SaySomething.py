#!/usr/bin/env python3

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
import time

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        # robot.behavior.say_text("Hello ")
        # robot.anim.play_animation('anim_eyepose_furious')
        # robot.anim.play_animation('anim_movement_forward_01')
        robot.anim.play_animation('anim_eyepose_sad_up')
        # robot.behavior.say_text("Michael")
        # robot.behavior.say_text("Clinton")
        # robot.behavior.say_text("Jenny")
        # robot.behavior.say_text("I am missing you")
        # robot.anim.play_animation('anim_eyepose_sad_down')

        # robot.audio.stream_wav_file('/Users/tg415h/Downloads/cat.wav')
        # print("Say 'Hello World'...")
        # robot.anim.play_animation('anim_movement_forward_01')
        # robot.anim.play_animation('anim_eyepose_furious')
        # robot.behavior.say_text("Ae Aai ghalia")
        # robot.behavior.say_text("aai zawadyaa")
        # robot.behavior.say_text("Behenchaoad")
        # robot.behavior.say_text("Chuteya")
        # robot.anim.play_animation('anim_fistbump_success_03')







if __name__ == "__main__":
    main()
