#!/usr/bin/env python3
print("""
Check colour
""")


import flotilla
import time
import sys

COLOR_INFO = "{red},{green},{blue},{clear}"
client = flotilla.Client()

print("Client connected...")

while not client.ready:
    pass

print("Finding colour module...")

color = client.first(flotilla.Colour)

if color is None:
    client.stop()
    sys.exit(1)

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
    client.stop()
