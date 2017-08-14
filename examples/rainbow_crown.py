#!/usr/bin/env python

# Eurovision crown - rainbow lights program
# Script by Tanya Fish x

import colorsys
import sys
import time

import flotilla


# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
dial = dock.first(flotilla.Joystick)
rainbow = dock.first(flotilla.Matrix)

if dial is None or rainbow is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Sets the start colour for the lights
hue = 0
pos = 0

# This is the loop that keeps moving through the rainbow,
# and checks Dial to decide how many pixels to light up.
# The module.is_a() method is used to apply the effect to
# ALL modules of type Rainbow attached to the dock.

try:
    while True:
        r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]

        for module in dock.available.values():
            if module.is_a(flotilla.Dial):
                pos = int((module.position / 1023.0) * 5)
            if module.is_a(flotilla.Rainbow):
                for x in range(module.num_pixels):
                    if x < pos:
                        module.set_pixel(x, r, g, b)
                    else:
                        module.set_pixel(x, 0, 0, 0)
                module.update()

        hue+=1
        hue%=360

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
