import time

import anki_vector
import requests
import json

from anki_vector.events import Events
from anki_vector.faces import Face

from anki_vector.util import degrees
import threading
import datetime

CONST_JOKE_INTERVAL_SECS = 20
CONST_PROGRAM_RUNTIME_SECS = 130.0

LAST_INTERACTION = datetime.datetime.now() - datetime.timedelta(seconds=40)


def tell_joke(robot):
    global LAST_INTERACTION
    response = requests.get("http://api.icndb.com/jokes/random?")
    if response.status_code == 200:
        joke = str(json.loads(response.content)["value"]["joke"])
        robot.conn.request_control()
        try:
            print(joke)
            robot.behavior.say_text(joke)
            LAST_INTERACTION = datetime.datetime.now()
            robot.anim.play_animation("anim_eyecontact_giggle_01")
            robot.behavior.set_head_angle(degrees(45.0))
            robot.behavior.set_lift_height(0.0)
        except:
            print("Exception occurred while saying the joke")


def on_object_observed(robot, event_type, event, evt):
    global LAST_INTERACTION
    interval = (datetime.datetime.now() - LAST_INTERACTION).total_seconds()
    if interval > CONST_JOKE_INTERVAL_SECS:
        if event.name:
            robot.behavior.say_text(f"Hello {event.name}")
        tell_joke(robot)
    else:
        print(f"{interval} seconds since last joke")


with anki_vector.Robot(enable_face_detection=True) as robot:
    # If necessary, move Vector's Head and Lift to make it easy to see his face
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)

    evt = threading.Event()
    robot.events.subscribe(on_object_observed, Events.robot_observed_face, evt)

    print("------ waiting for face events, press ctrl+c to exit early ------")

    try:
        if not evt.wait(timeout=CONST_PROGRAM_RUNTIME_SECS):
            print("------ Vector never saw your face! ------")
    except KeyboardInterrupt:
        pass

robot.events.unsubscribe(on_object_observed, Events.robot_observed_face)
