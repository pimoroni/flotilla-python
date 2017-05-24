#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


# message comes up when you run the program to show how to stop
print("""
This example will show the temperature in degrees centigrade on the Number display, and the barometer reading on the Rainbow display. Press CTRL + C to exit.
""")

#renames dock
dock = flotilla.Client()

#looks for the first number display and calls it something more recognisable
#does the same for the first rainbow it finds
first_number_display = dock.first(flotilla.Number)
first_rainbow = dock.first(flotilla.Rainbow)


#looks for a weather module and displays the temperature on the number block
#checks the pressure and shows it on the rainbow
try:
    while True:
        weather = dock.first(flotilla.Weather)
        light = dock.first(flotilla.Light)

        if weather:
            tempr = weather.temperature
            first_number_display.set_number(int(tempr))
            first_number_display.update()

        if light:
            brightness=light.light

            if brightness > 100:
                first_rainbow.set_pixel (0, 0, 255, 0)
            if brightness > 250:
                first_rainbow.set_pixel (1, 0, 255, 0)
            if brightness > 400:
                first_rainbow.set_pixel (2, 0, 255, 0)
            if brightness > 550:
                first_rainbow.set_pixel (3, 0, 255, 0)
            if brightness > 700:
                first_rainbow.set_pixel (4, 0, 255, 0)

            first_rainbow.update()

        time.sleep(0.9)

        for x in range(first_rainbow.num_pixels):
            first_rainbow.set_pixel (x, 0, 0, 0)

        first_rainbow.update()


#allows you to stop the program with ctrl and c
except KeyboardInterrupt:

    dock.stop()
