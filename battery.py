import anki_vector

with anki_vector.Robot() as robot:
    battery_levels = {1:"low", 2:"nomial", 3:"full"}
    battery_state = robot.get_battery_state()
    if battery_state:
        robot.behavior.say_text("Current battery status is {:.1f} volts which is {}. I need {:.0f} more seconds to charge".format(battery_state.battery_volts, battery_levels[battery_state.battery_level], battery_state.suggested_charger_sec))
        print("Robot battery voltage: {0}".format(battery_state.battery_volts))
        print("Robot battery Level: {0}".format(battery_state.battery_level))
        print("Robot suggested charger time: {0}".format(battery_state.suggested_charger_sec))
    else:
        robot.behavior.say_text("Cannot get battery status right now")
