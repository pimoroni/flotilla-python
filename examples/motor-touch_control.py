#!usr/bin/env/python

# This code is for the Flotilla Motor and Touch modules,
# and in my model uses a turntable attached to the Motor
# Script by Tanya Fish x

import time
import sys

import flotilla


# Looks for the dock, and all of the modules we need attached to the dock so we can talk to them

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
motor = dock.first(flotilla.Motor)
touch = dock.first(flotilla.Touch)

if motor is None or touch is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Starts the loop going so it keeps working until we stop it
try:
    while True:

# Looks for a Touch module and listens for an input
# Makes the motor move to rotate the treat wheel to the right treat,
# and waits 10 secs for you to grab it
# Rotates the treat wheel back to the start position.

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

# This listens for a keyboard interrupt, which is Ctrl+C and can stop the program
except KeyboardInterrupt:
    dock.stop()
