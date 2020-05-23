import csv
import anki_vector
import time

args = anki_vector.util.parse_command_args()

with open('vector_animations.csv', newline='') as csv_file, anki_vector.Robot(args.serial) as robot:
    iterator = csv.reader(csv_file, delimiter=',')
    csv_data_list = list(iterator)
    for i in range(200, 301):
        print(csv_data_list[i][0])
        robot.behavior.say_text(str(i))
        robot.anim.play_animation(csv_data_list[i][0])
        time.sleep(0.3)
