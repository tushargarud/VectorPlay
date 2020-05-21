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
Display camera feed on face
"""

import anki_vector
import time

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.vision.enable_display_camera_feed_on_face()
        time.sleep(10.0)

if __name__ == "__main__":
    main()
