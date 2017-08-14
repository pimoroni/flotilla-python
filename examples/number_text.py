#!/usr/bin/env python

import sys
import time

import flotilla


print("""
This example will display text on the Number display.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
number = dock.first(flotilla.Number)

if number is None:
    print("no Number module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. String displayed...")

number.set_brightness(128)
number.set_string("yarr")
number.update()
time.sleep(1)
dock.stop()

