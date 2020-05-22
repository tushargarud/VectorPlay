import anki_vector
from anki_vector.events import Events
from anki_vector.util import degrees
import threading

said_text = False

def on_robot_observed_face(robot, event_type, event, evt):
    print(f"Vector sees a face:{evt}\n")
    global said_text
    if not said_text:
        said_text = True
        robot.behavior.say_text("I see a face!")
        evt.set()

with anki_vector.Robot(enable_face_detection=True) as robot:

    # If necessary, move Vector's Head and Lift to make it easy to see his face
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)

    evt = threading.Event()
    robot.events.subscribe(on_robot_observed_face, Events.robot_observed_face, evt)

    print("------ waiting for face events, press ctrl+c to exit early ------")

    try:
        if not evt.wait(timeout=120.0):
            print("------ Vector never saw your face! ------")
    except KeyboardInterrupt:
        pass

robot.events.unsubscribe(on_robot_observed_face, Events.robot_observed_face)