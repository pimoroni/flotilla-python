#!/usr/bin/env python

import flotilla
import time
import colorsys

client = flotilla.Client(
        requires={
            'eight': flotilla.Rainbow
        }
    )

hue = 0

try:
    while True:
        r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]

        for module in client.available.values():
            if module.is_a(flotilla.Rainbow):
                for x in range(module.num_pixels):
                    module.set_pixel(x, r, g, b)
                module.update()

        hue+=1
        hue%=360
        time.sleep(0.1)

except KeyboardInterrupt:
    client.stop()
