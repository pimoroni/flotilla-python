#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


print("""
This example displays the temperature in degrees centigrade on the Number module,
and a light level reading from a Ligh module on the Rainbow module.

Press CTRL + C to exit.
""")

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
light = dock.first(flotilla.Light)
number = dock.first(flotilla.Number)
rainbow = dock.first(flotilla.Rainbow)
weather = dock.first(flotilla.Weather)

if light is None or number is None or rainbow is None or weather is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Looks for a Weather module and displays the temperature on a Number module.
# It also checks the light level using a Light module and shows it on a Rainbow module.

r = 0
g = 255
b = 0

try:
    while True:
        if weather:
            temp = weather.temperature
            number.set_number(int(temp))
            number.update()
        if light:
            brightness=light.light
            if brightness > 100 and brightness < 249:
                for p in range(1):
                    rainbow.set_pixel (p, r, g, b)
            elif brightness > 250 and brightness < 399:
                for p in range(2):
                    rainbow.set_pixel (p, r, g, b)
            elif brightness > 400 and brightness < 549:
                for p in range(3):
                    rainbow.set_pixel (p, r, g, b)
            elif brightness > 550 and brightness < 699:
                for p in range(4):
                    rainbow.set_pixel (p, r, g, b)
            elif brightness > 700:
                for p in range(5):
                    rainbow.set_pixel (p, r, g, b)
            rainbow.update()

        time.sleep(0.9)

        for x in range(rainbow.num_pixels):
            rainbow.set_pixel (x, 0, 0, 0)

        rainbow.update()

except KeyboardInterrupt:
    dock.stop()
