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
Show am image on vector's screen
"""

import anki_vector
import time
from PIL import Image

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        image_file = Image.open('/Users/tg415h/bear.jpg')
        screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
        robot.screen.set_screen_with_image_data(screen_data, 4.0)
        time.sleep(4.0)

if __name__ == "__main__":
    main()
