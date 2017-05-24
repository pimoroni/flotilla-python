#!/usr/bin/env python

# gets information about time and how flotilla works
import time
import flotilla

# message comes up when you run the program to show how to stop
print("""
This example will show the temperature in degrees centigrade on the Number display. Press CTRL + C to exit.
""")

#renames the dock
dock = flotilla.Client()

#looks for the first number display and calls it something more recognisable
first_number_display = dock.first(flotilla.Number)

#looks for a weather module and displays the temperature on the number block
try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Weather):


                tempr = module.temperature
                first_number_display.set_number(int(tempr))
                first_number_display.update()

        time.sleep(0.5)
except KeyboardInterrupt:
    dock.stop()
