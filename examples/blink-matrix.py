#!/usr/bin/env python3

import time

import flotilla

print("""
This example will iterate through all connected Flotilla modules,
find each Matrix, and blink one of the pixels.

It demonstrates how to find connected modules and identify a module by type.

Press CTRL+C to exit.
""")

c = flotilla.Client()

state = True

try:
    while True:
        for module in c.available.values():
            if module.is_a(flotilla.Matrix):
                module.set_pixel(1, 1, state).update()

        state = not state
        time.sleep(1)

except KeyboardInterrupt:
    c.stop()
