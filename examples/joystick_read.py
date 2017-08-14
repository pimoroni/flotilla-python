#!/usr/bin/env python

import sys
import time

import flotilla


print("""
Reading Joystick coordinates.

Press CTRL+C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
joystick = dock.first(flotilla.Joystick)

if joystick is None:
    print("no Joystick module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

tolerance = 20

try:
    while True:
        print(joystick.data)
        joyxysum=joystick.x+joystick.y
        time.sleep(0.5)
        joyxycheck=joystick.x+joystick.y
        if joystick.x <= tolerance:
            print("Joystick pointing left")
        elif joystick.x >= 1023-tolerance:
            print("Joystick pointing right")
        elif joystick.y <= tolerance:
            print("Joystick pointing downwards")
        elif joystick.y >= 1023-tolerance:
            print("Joystick pointing upwards")
        elif joyxysum >= 1024 and joyxysum <= 1096+tolerance and joyxysum == joyxycheck:
            print("Joystick at rest")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
