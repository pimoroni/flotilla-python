#!/usr/bin/env python

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
dial = dock.first(flotilla.Dial)
rainbow = dock.first(flotilla.Rainbow)

if dial is None or rainbow is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Reads Dial module value. First half of dial = bad day, 2nd half = awful.
# If bad, lights up a motivational message with a rainbow. If awful, delivers treat also.
# This is the Rainbow sequence from the examples, and applied to all Rainbow modules attached.

hue = 0
pos = 0

try:
    while True:
        r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]

        # Lights up the Rainbow module if Dial is over 100 but strictly under 512.
        pos = int(module.position)
        if module.is_a(flotilla.Rainbow):
            for x in range(module.num_pixels):
                if 100 < pos < 512:
                    module.set_pixel(x, r, g, b)
                else:
                    module.set_pixel(x, 0, 0, 0)
            module.update()

        hue+=1
        hue%=360

# Puts the motor on for 2 seconds if the dial is above 512
        if module.is_a(flotilla.Motor):
            if pos > 512:
                module.set_speed(20)
                time.sleep(2)
                module.stop()

# Makes the Number module show you / rule / (blank) or be/cool/(blank) on a cycle.
# The spaces are important otherwise the display doesn't clear.
        if module.is_a(flotilla.Number):
            if 100 < pos <= 512:
                    module.set_brightness(128)
                    module.set_string(" you")
                    module.update()
                    time.sleep(1)
                    module.set_string("rule")
                    module.update()
                    time.sleep(1)
                    module.set_string("    ")
                    module.update()
                    time.sleep(1)
            elif pos > 512:
                    module.set_brightness(128)
                    module.set_string(" be ")
                    module.update()
                    time.sleep(1)
                    module.set_string("cool")
                    module.update()
                    time.sleep(1)
                    module.set_string("    ")
                    module.update()
                    time.sleep(1)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
