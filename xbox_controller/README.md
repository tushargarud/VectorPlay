# Vector Controller

Vector Controller is a WIP program for Anki Vector that uses a gamepad and the inputs library for python.

Vector Controller works with any gamepad connected to a computer. If you have the Vector SDK installed and set up, run `py main.py` and you're all set!

### Current Controls

`[A Button/BTN_SOUTH]`: Move vector's lift up and then down quickly

`[Dpad Up/ABS_HATOY state -1]`: Move vector's lift up and hold it there

`[Dpad Down/ABS_HATOY state 1]`: Move vector's lift down

`[Left Joystick up/ABS_Y state <= +-3000]`: Move vector forward or backwards

`[Right Joystick sideways/ABS_RX state <= +-3000]`: Turn vector 45 degrees

`[Back button (on logitech controllers)/BTN_START state 1]`: Exit program
