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
from PIL import Image
from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.behavior import util
from anki_vector import audio
import time


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.AsyncRobot() as robot:
        robot.behavior.set_head_angle(util.degrees(30.0))
        image_file = Image.open('/home/pi/vector_programs/VectorPlay/images/chevy.jpg')
        screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
        three_future = robot.screen.set_screen_with_image_data(screen_data, 15.0)
        one_future = robot.audio.stream_wav_file('/home/pi/vector_programs/VectorPlay/sounds/camaro_long.wav', 100)
        two_future = robot.motors.set_wheel_motors(10, 10, 65, 65)
        time.sleep(4.8)
        four_future = robot.motors.set_wheel_motors(150, 150)
        time.sleep(2)
        four_future = robot.motors.set_wheel_motors(5, 200)
        time.sleep(8)

if __name__ == "__main__":
    main()
