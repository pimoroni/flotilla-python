import time
import flotilla

#displays a message to show how to stop the program
print("""
This example will show the air pressure on the Rainbow display. Use overlay for meaning. Press CTRL + C to exit.
""")

#gives the dock a nicer name
dock=flotilla.Client()

#names the first rainbow it finds
first_rainbow=dock.first(flotilla.Rainbow)

#looks for a weather module and measures the air pressure as pressure
#decides which pixels to light up depending on pressure
#lights up right number of pixels, then clears for next round
#repeats every half a second until interrupted with ctrl and c

try:
    while True:

        for module in dock.available.values():
            if module.is_a(flotilla.Weather):

                pressure=module.pressure

                if pressure >= 10150:
                    first_rainbow.set_pixel (0, 255, 0, 0)
                elif pressure > 9850:
                    first_rainbow.set_pixel (2, 0, 255, 0)
                elif pressure > 8000:
                    first_rainbow.set_pixel (4, 0, 0, 255)

                first_rainbow.update()

        time.sleep(0.5)
        for x in range(first_rainbow.num_pixels):
            first_rainbow.set_pixel (x, 0, 0, 0)

except KeyboardInterrupt:
                dock.stop()
