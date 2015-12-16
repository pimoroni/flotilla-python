print("""
This example requires a Touch and Rainbow module,
you'll find these in the mini kit.

Use the buttons on the Touch module to control
your mood lighting!

Press Ctrl+C to exit.
""")

import colorsys
import flotilla
import time

client = flotilla.Client(
   requires={
        'one': flotilla.Touch,
        'eight': flotilla.Rainbow
    })

def module_changed(channel, module):
    rainbow = client.first(flotilla.Rainbow)
    if module.is_a(flotilla.Touch):
        if module.one:
            rainbow.set_pixel(0,255,0,0).update()
        else:
            rainbow.set_pixel(0,0,0,0).update()

#client.module_changed = module_changed

while not client.ready:
    pass

touch = client.first(flotilla.Touch)
rainbow = client.first(flotilla.Rainbow)
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
        if touch.four:
            lights_on = not lights_on

        r, g, b = 0, 0, 0
        if lights_on:
            r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]
        
        rainbow.set_all(r, g, b).update()

        #print("Hue: {hue}, RGB: {r},{g},{b}".format(
        #hue=hue, r=r, g=g, b=b))

        time.sleep(0.1)
except KeyboardInterrupt:
    client.stop()
