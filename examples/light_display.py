#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


#displays a message to show how to stop the program
print("""
This example will show the light level on the Number display. Press CTRL + C to exit.
""")

#renames the dock to a nicer name
dock = flotilla.Client()

#tells it to call the first flotilla number module the first number display
first_number_display = dock.first(flotilla.Number)

#reads the light level from the light module and displays it as a whole number
#on the first number display. Repeats every half a second.

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Light):


                brightness = module.light
                first_number_display.set_number(int(brightness))
                first_number_display.update()

        time.sleep(0.5)
except KeyboardInterrupt:
    dock.stop()
