#!/usr/bin/env python3

import time
from random import randint

import flotilla


print("""
This example will display text on the Number display
""")

client = flotilla.Client()

first_number_display = client.first(flotilla.Number)

if first_number_display is not None:
    first_number_display.set_brightness(128)
    first_number_display.set_string("yarr")
    first_number_display.update()
    time.sleep(1)
else:
    print("You must connect a Number first!")

client.stop()

