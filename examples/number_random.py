#!/usr/bin/env python

import sys
import time
from random import randint

import flotilla


print("""
This example will display random numbers on the Number display.

Press CTRL+C to exit.
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
    print("Found. Running...")

try:
    while True:
        random_number = randint(0,9999)
        number.set_number(random_number)
        number.update()
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
