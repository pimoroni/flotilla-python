#work in progress - not finished

#this imports the time library so it can time how long the motor is on for
#also imports the flotilla library so it can operate the modules
import time
import flotilla
import sys

#looks for the dock, and all of the modules we need attached to the dock so we can talk to them
dock = flotilla.Client()
motor = dock.first(flotilla.Motor)
touch = dock.first(flotilla.Touch)

current_offset=0
def go_to_offset(offset):
    target_offset=offset-current_offset
    motor.set_speed(target_offset)
    time.sleep(1)
    motor.stop()
    current_offset=target_offset

go_to_offset(10)
go_to_offset(-10)
