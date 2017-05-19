#!/usr/bin/env python

import sys
import time

import flotilla


print("""
This example will iterate through all connected Flotilla modules,
find each Matrix, and blink one of the pixels.

Press CTRL+C to exit.
""")

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
matrix = dock.first(flotilla.Matrix)

if matrix is None:
    print("no Matrix module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")


state = True

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Matrix):
                module.set_pixel(3, 3, state).update()

        state = not state
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
