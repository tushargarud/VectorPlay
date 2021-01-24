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


import anki_vector
from anki_vector.util import degrees
import time

with anki_vector.AsyncRobot() as robot:
    say_future = robot.audio.stream_wav_file('/home/pi/vector_programs/VectorPlay/sounds/cat.wav', 100)
    turn_future = robot.behavior.look_around_in_place()
    say_future.result()
    turn_future.cancel()
