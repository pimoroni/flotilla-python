#!/usr/bin/env python

import colorsys
import sys
import time

import flotilla


print("""
This example will iterate through all connected Flotilla modules,
find each Rainbow, and turn them into beautiful mood lights.

Press CTRL+C to exit.
""")

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
rainbow = dock.first(flotilla.Rainbow)

if rainbow is None:
    print("no Rainbow module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

hue = 0

try:
    while True:
        r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]

        for module in dock.available.values():
            if module.is_a(flotilla.Rainbow):
                for x in range(module.num_pixels):
                    module.set_pixel(x, r, g, b)
                module.update()
        hue+=1
        hue%=360
        time.sleep(0.1)

except KeyboardInterrupt:
    dock.stop()
