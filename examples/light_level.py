import time
import flotilla

#displays a message to show how to stop the program
print("""
This example will show the light level on the Rainbow display. Press CTRL + C to exit.
""")

#gives the dock a nicer name
dock=flotilla.Client()

#names the first rainbow it finds
first_rainbow=dock.first(flotilla.Rainbow)

#looks for a light module and measures the light as brightness
#decides which pixels to light up depending on brightness
#lights up right number of pixels, then clears for next round
#repeats every half a second until interrupted with ctrl and c

try:
    while True:

        for module in dock.available.values():
            if module.is_a(flotilla.Light):

                brightness=module.light

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

        time.sleep(0.5)
        for x in range(first_rainbow.num_pixels):
            first_rainbow.set_pixel (x, 0, 0, 0)

except KeyboardInterrupt:
                dock.stop()
