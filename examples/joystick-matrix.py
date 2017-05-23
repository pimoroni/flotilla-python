#!/usr/bin/env python

import sys
import time

import flotilla


print("""
This example shows you how to control the Matrix with a Joystick module.

Press CTRL+C to exit.
""")

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
matrix = dock.first(flotilla.Matrix)
joystick = dock.first(flotilla.Joystick)

if matrix is None or joystick is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

try:
    while True:
        matrix.clear()
        xpixel = int(joystick.x/128)
        ypixel = int(joystick.y/128)
        matrix.set_pixel(xpixel, ypixel, 1).update()

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
