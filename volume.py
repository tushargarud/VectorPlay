import anki_vector
from anki_vector import audio
import argparse
import time
from anki_vector.util import degrees, distance_mm, speed_mmps

parser = argparse.ArgumentParser()
parser.add_argument("volume_value")
args = anki_vector.util.parse_command_args(parser)

with anki_vector.Robot(args.serial) as robot:
    volume = args.volume_value
    if volume == '0' or volume == 'low':
        volume_enum = audio.RobotVolumeLevel.LOW
    elif volume == '1' or volume == 'medium low':
        volume_enum = audio.RobotVolumeLevel.MEDIUM_LOW
    elif volume == '2' or volume == 'medium':
        volume_enum = audio.RobotVolumeLevel.MEDIUM
    elif volume == '3' or volume == 'medium high':
        volume_enum = audio.RobotVolumeLevel.MEDIUM_HIGH
    elif volume == '4' or volume == 'high':
        volume_enum = audio.RobotVolumeLevel.HIGH        

    robot.audio.set_master_volume(volume_enum)
    robot.behavior.say_text(f"Volume set to {volume}")
