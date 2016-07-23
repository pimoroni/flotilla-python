#!/usr/bin/env python

import flotilla
import time
from random import randint

print("""
This example will display random numbers on the Number display
""")

client = flotilla.Client()

first_number_display = client.first(flotilla.Number)
try:
    while True:
        random_number = randint(0,9999)
        first_number_display.set_number(random_number)
        first_number_display.update()

        time.sleep(0.5)
except KeyboardInterrupt:
    client.stop()

