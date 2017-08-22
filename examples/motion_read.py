#!/usr/bin/env python

import sys
import time

import flotilla


print("""
Reading Motion values.

Press CTRL+C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
motion = dock.first(flotilla.Motion)

if motion is None:
    print("no Motion module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

MOTION_INFO = "{x},{y},{z} Heading: {h}"

try:
    while True:
        print(MOTION_INFO.format(
            x=motion.x,
            y=motion.y,
            z=motion.z,
            h=motion.heading))
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
