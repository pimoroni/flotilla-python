#!/usr/bin/env python

import colorsys
import sys
import time

import flotilla


print("""
This example requires a Touch and Rainbow module,
you'll find these in the mini kit.

Use the buttons on the Touch module to control
your mood lighting!

1 hue -
2 hue +
3 preset
4 on/off

Press Ctrl+C to exit.
""")

try:
    dock = flotilla.Client(
       requires={
            'one': flotilla.Touch,
            'two': flotilla.Rainbow
        })
except KeyboardInterrupt:
    sys.exit(1)

while not dock.ready:
    pass

touch = dock.first(flotilla.Touch)
rainbow = dock.first(flotilla.Rainbow)
hue = 0
lights_on = True

try:
    while True:
        if touch.one:
            hue -= 4
            hue %= 360
        if touch.two:
            hue += 4
            hue %= 360
        if touch.three:
            hue += 60
            hue %= 360
        if touch.four:
            lights_on = not lights_on
        r, g, b = 0, 0, 0
        if lights_on:
            r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]
        rainbow.set_all(r, g, b).update()
        time.sleep(0.1)
except KeyboardInterrupt:
    dock.stop()
