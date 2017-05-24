#!/usr/bin/env python

# gets information about time and how flotilla works
import time
import flotilla

# message comes up when you run the program to show how to stop
print("""
This example will show the temperature in degrees centigrade on the Number display, and the barometer reading on the Rainbow display. Press CTRL + C to exit.
""")

#renames the flotilla client so it's shorter to type
dock = flotilla.Client()

#looks for the first number display and calls it something more recognisable
#does the same for the first rainbow it finds
first_number_display = dock.first(flotilla.Number)
first_rainbow = dock.first(flotilla.Rainbow)


#looks for a weather module and displays the temperature on the number block
#checks the pressure and shows it on the rainbow
try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Weather):


                tempr = module.temperature
                first_number_display.set_number(int(tempr))
                first_number_display.update()

                pressure = module.pressure
                if pressure > 10150:
                    first_rainbow.set_pixel (0, 255, 0, 0)
                elif pressure > 9850:
                    first_rainbow.set_pixel (2, 0, 255, 0)
                elif pressure > 8000:
                    first_rainbow.set_pixel (4, 0, 0, 255)

                first_rainbow.update()

        time.sleep(0.5)

        for x in range(first_rainbow.num_pixels):
            first_rainbow.set_pixel (x, 0, 0, 0)

#allows you to stop the program with ctrl and c
except KeyboardInterrupt:
    dock.stop()
