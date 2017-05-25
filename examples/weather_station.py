#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


print("""
This example will show the temperature in degrees centigrade on the Number display, and the barometer reading on the Rainbow display. Press CTRL + C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
number = dock.first(flotilla.Number)
rainbow = dock.first(flotilla.Rainbow)

if number is None or rainbow is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Looks for a weather module and displays the temperature on the Number module
# Checks the pressure and shows it on the rainbow.

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Weather):
                temp = module.temperature
                number_display.set_number(int(temp))
                number_display.update()

                pressure = module.pressure
                if pressure > 10150:
                    rainbow.set_pixel (0, 255, 0, 0)
                elif pressure > 9850:
                    rainbow.set_pixel (2, 0, 255, 0)
                elif pressure > 8000:
                    rainbow.set_pixel (4, 0, 0, 255)

                rainbow.update()

        time.sleep(0.5)

        for x in range(rainbow.num_pixels):
            rainbow.set_pixel (x, 0, 0, 0)

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
