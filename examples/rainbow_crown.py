#!/usr/bin/env python

# Eurovision crown - rainbow lights program
# Script by Tanya Fish x

import colorsys
import sys
import time

import flotilla


#gives a nice name to the dock
dock = flotilla.Client()

#sets the start colour for the lights
hue = 0
pos = 0

#this is the loop that keeps moving through the rainbow, and checks the dial to
#see how many pixels to light up
#using if module.is_a thing means it applies to ALL modules of that type

try:
    while True:
        r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]

        for module in dock.available.values():
            if module.is_a(flotilla.Dial):
                pos = int((module.position / 1023.0) * 5)
            if module.is_a(flotilla.Rainbow):
                for x in range(module.num_pixels):
                    if x < pos:
                        module.set_pixel(x, r, g, b)
                    else:
                        module.set_pixel(x, 0, 0, 0)
                module.update()

        hue+=1
        hue%=360

#gives you the option to stop the program with ctrl+c
except KeyboardInterrupt:
    dock.stop()
