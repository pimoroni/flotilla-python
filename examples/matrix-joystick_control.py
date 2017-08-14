#!/usr/bin/env python

import sys
import time

import flotilla


print("""
This example shows you how to control the Matrix with a Joystick module.

Press CTRL+C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
joystick = dock.first(flotilla.Joystick)
matrix = dock.first(flotilla.Matrix)

if joystick is None or matrix is None:
    print("Some modules required were not found...")
    print("Make sure you have a Joystick and a Matrix module attached to the Dock!")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

joystick.rotation(0)
matrix.rotation(0)

try:
    while True:
        matrix.clear()
        xpixel = int(joystick.x/128)
        ypixel = int(joystick.y/128)
        matrix.set_pixel(xpixel, ypixel, 1).update()

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
