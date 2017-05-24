#!usr/bin/env/python
#this code is for the Flotilla Motor and Touch modules, and in my model uses a turntable attached to the Motor

#apologies for all the notes. Tanya Fish x

#this imports the time library so it can time how long the motor is on for
#also imports the flotilla library so it can operate the modules
import time
import flotilla
import sys

#looks for the dock, and all of the modules we need attached to the dock so we can talk to them
dock = flotilla.Client()
motor = dock.first(flotilla.Motor)
touch = dock.first(flotilla.Touch)

#starts the loop going so it keeps working until we stop it
try:
    while True:

#looks for a Touch module and listens for an input
#makes the motor move to rotate the treat wheel to the right treat, and waits 10 secs for you to grab it
#rotates the treat wheel back to the start position

        if touch.one:
            motor.set_speed(20)
            time.sleep(1)
            motor.stop()
            time.sleep(10)
            motor.set_speed(-20)
            time.sleep(1)
            motor.stop()

        if touch.two:
            motor.set_speed(20)
            time.sleep(2)
            motor.stop()
            time.sleep(10)
            motor.set_speed(-20)
            time.sleep(2)
            motor.stop()

        if touch.three:
            motor.set_speed(20)
            time.sleep(3)
            motor.stop()
            time.sleep(10)
            motor.set_speed(-20)
            time.sleep(3)
            motor.stop()

        if touch.four:
            motor.set_speed(20)
            time.sleep(4)
            motor.stop()
            time.sleep(10)
            motor.set_speed(-20)
            time.sleep(4)
            motor.stop()
#this listens for a keyboard interrupt, which is Ctrl+C and can stop the program
except KeyboardInterrupt:
    dock.stop()
