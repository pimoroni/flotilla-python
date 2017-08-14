#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


print("""
This example will display the air pressure on the Rainbow module.

Press CTRL + C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
rainbow = dock.first(flotilla.Rainbow)
weather = dock.first(flotilla.Weather)

if rainbow is None or weather is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Looks for a Weather module and measures the air pressure
# to decide which pixels to light up depending on measurement.
# Lights up right number of pixels, then clears for next round.
# Repeats every half a second until interrupted by user.

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Weather):

                pressure=module.pressure

                if pressure >= 10150:
                    rainbow.set_pixel (0, 255, 0, 0)
                elif pressure > 9850:
                    rainbow.set_pixel (2, 0, 255, 0)
                elif pressure > 8000:
                    rainbow.set_pixel (4, 0, 0, 255)

                rainbow.update()

        time.sleep(0.5)
        for x in range(rainbow.num_pixels):
            rainbow.set_pixel (x, 0, 0, 0)

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
