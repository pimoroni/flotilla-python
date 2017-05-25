#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


print("""
This example will read the light level from a Light module
and display it on a Rainbow module to reflect measurement.

Press CTRL + C to exit.
""")

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
light = dock.first(flotilla.Light)
rainbow = dock.first(flotilla.Rainbow)

if light is None or rainbow is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")


# Looks for a light module and measures the light as brightness
# to decide which pixels to light up depending on reading
# Lights up right number of pixels, then clears for next round.
# Repeats every half a second until interrupted with CTRL + C.

r = 192
g = 64
b = 0

try:
    while True:

        for module in dock.available.values():
            if module.is_a(flotilla.Light):

                brightness = module.light

                if brightness > 100:
                    rainbow.set_pixel (0, r, g, b)
                if brightness > 250:
                    rainbow.set_pixel (1, r, g, b)
                if brightness > 400:
                    rainbow.set_pixel (2, r, g, b)
                if brightness > 550:
                    rainbow.set_pixel (3, r, g, b)
                if brightness > 700:
                    rainbow.set_pixel (4, r, g, b)

            rainbow.update()

        time.sleep(0.5)
        for x in range(rainbow.num_pixels):
            rainbow.set_pixel (x, 0, 0, 0)

except KeyboardInterrupt:
    dock.stop()
