#!/usr/bin/env python
#joymachine

#needs to know about time and the flotilla modules, and colours
import time
import flotilla
import colorsys

#shortens the name of the thing that runs Flotilla
dock = flotilla.Client()

#looks for output from dial. First half of dial = bad day, 2nd half = awful
# if bad, lights up a motivational message with a rainbow. if awful, delivers treat also.

#this is the rainbow sequence from the examples, and applied to all of the Rainbow modules attached
hue = 0
pos = 0

try:
    while True:
        r, g, b = [int(x * 255.0) for x in colorsys.hsv_to_rgb(hue/360.0, 1.0, 1.0)]

#puts the rainbow on if the dial is over 100 and under 512 - it's off under 100 or over 512
        for module in dock.available.values():
            if module.is_a(flotilla.Dial):
                pos = int(module.position)
            if module.is_a(flotilla.Rainbow):
                for x in range(module.num_pixels):
                    if 100 < pos < 512:
                        module.set_pixel(x, r, g, b)
                    else:
                        module.set_pixel(x, 0, 0, 0)
                module.update()

        hue+=1
        hue%=360

#puts the motor on for 2 seconds if the dial is above 513
        for module in dock.available.values():
            if module.is_a(flotilla.Dial):
                pos = int(module.position)
            if module.is_a(flotilla.Motor):
                if 513 < pos < 1024:
                        module.set_speed(20)
                        time.sleep(2)
                        module.stop()

#makes the Number display show you / rule / (blank) or be/cool/(blank) on a cycle.
#The spaces are important otherwise the display doesn't clear
        for module in dock.available.values():
            if module.is_a(flotilla.Dial):
                pos = int(module.position)
            if module.is_a(flotilla.Number):
                if 100 < pos < 512:
                        module.set_brightness(128)
                        module.set_string(" you")
                        module.update()
                        time.sleep(1)
                        module.set_string("rule")
                        module.update()
                        time.sleep(1)
                        module.set_string("    ")
                        module.update()
                        time.sleep(1)
        for module in dock.available.values():
            if module.is_a(flotilla.Dial):
                pos = int(module.position)
            if module.is_a(flotilla.Number):
                if 513 < pos < 1024:
                        module.set_brightness(128)
                        module.set_string(" be ")
                        module.update()
                        time.sleep(1)
                        module.set_string("cool")
                        module.update()
                        time.sleep(1)
                        module.set_string("    ")
                        module.update()
                        time.sleep(1)

#insert bit here than then exits the program and switches everything off

except KeyboardInterrupt:
    dock.stop()
