import anki_vector

args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
    robot.anim.play_animation('anim_blackjack_ok_01')