#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


print("""
This example will show the light level on the Number display.

Press CTRL + C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
light = dock.first(flotilla.Light)
number = dock.first(flotilla.Number)

if light is None or number is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Reads the light level from a Light module and displays it as a whole number
# on the first Number module available. Repeats every half a second.

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Light):

                brightness = module.light
                number.set_number(int(brightness))
                number.update()
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
