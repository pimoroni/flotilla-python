#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


print("""
This example displays the temperature in degrees centigrade on the Number module.

Press CTRL + C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
number = dock.first(flotilla.Number)
weather = dock.first(flotilla.Weather)

if number is None or weather is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Weather):

                temp = module.temperature
                number.set_number(int(temp))
                number.update()

        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
