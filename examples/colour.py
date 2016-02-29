#!/usr/bin/env python3
print("""
Check colour
""")


import flotilla
import time

COLOR_INFO = "{red},{green},{blue},{clear}"
client = flotilla.Client()


while not client.ready:
    pass

color = client.first(flotilla.Colour)

try:
    while True:
        print(COLOR_INFO.format(
            red= color.red,
            green=color.green,
            blue=color.blue,
            clear=color.clear))
        time.sleep(0.5)
except KeyboardInterrupt:
    client.stop()
