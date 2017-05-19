#!/usr/bin/env python

import sys
import time

import flotilla


print("""
Reading Colour values.

Press CTRL+C to exit.
""")

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
color = dock.first(flotilla.Colour)

if color is None:
    print("no Colour module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

COLOR_INFO = "{red},{green},{blue},{clear}"

try:
    while True:
        print(COLOR_INFO.format(
            red= color.red,
            green=color.green,
            blue=color.blue,
            clear=color.clear))
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
