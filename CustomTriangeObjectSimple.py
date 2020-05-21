import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
import time
from anki_vector.events import Events
from anki_vector.util import degrees
import datetime
from PIL import Image


initial_height = 0
position = 'down'
position_changed_time = datetime.datetime.now()
whistle_count = 0
object_appeared_last_updated = datetime.datetime.now()

def handle_object_observed(robot, event_type, event):
    # print(f"--------- Vector observed an object --------- \n{event.obj}")
    global initial_height
    global position
    global position_changed_time
    global whistle_count

    if event.obj.archetype.custom_type.name == 'CustomType00':
        cur_height = event.obj.last_observed_image_rect.y_top_left

        if initial_height == 0:
            initial_height = cur_height

        print(f"\n position={position} --- height_moved={initial_height - cur_height} --- time since position changed  {(datetime.datetime.now() - position_changed_time).total_seconds()}  --------- ")

        if initial_height - cur_height > 5 and position == 'down' and (datetime.datetime.now() - position_changed_time).total_seconds() > 10:
            position = 'up'
            position_changed_time = datetime.datetime.now()
            print(f"--------- Wistle moved up  --------- \n{initial_height - cur_height}")
            robot.anim.play_animation('anim_qa_lift_updown')
            whistle_count += 1
            robot.behavior.say_text(f"wistle {whistle_count}")

            if whistle_count > 2:
                robot.events.unsubscribe(handle_object_observed, Events.object_observed)
                robot.behavior.say_text(f"{whistle_count} wistles complete. Turn off the cooker")
                robot.anim.play_animation('anim_fistbump_success_03')

                robot.behavior.set_head_angle(degrees(50.0))
                image_file = Image.open('/Users/tg415h/done.jpg')
                screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
                robot.screen.set_screen_with_image_data(screen_data, 10.0)
                time.sleep(10.0)

        elif position == 'up' and initial_height - cur_height < 5 and (datetime.datetime.now() - position_changed_time).total_seconds() > 10:
            position = 'down'
            position_changed_time = datetime.datetime.now()
            print(f"--------- Wistle moved down  --------- \n{initial_height - cur_height}")



with anki_vector.Robot(enable_custom_object_detection=True) as robot:
    robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType00,
                                   marker=CustomObjectMarkers.Triangles2,
                                   size_mm=20.0,
                                   marker_width_mm=29.0, marker_height_mm=29.0)

    # If necessary, move Vector's Head and Lift down
    robot.behavior.set_lift_height(0.0)
    robot.behavior.set_head_angle(degrees(30.0))

    robot.events.subscribe(handle_object_observed, Events.object_observed)

    time.sleep(3600.0)
