#!/usr/bin/env python

import sys
import time

import flotilla


print("""
This example will read the temperature and pressure from a Weather module.

Press CTRL+C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding module...")
weather = dock.first(flotilla.Weather)

if weather is None:
    print("no Weather module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

try:
    while True:
        print('Temp: {} Pressure: {}'.format(weather.temperature, weather.pressure))
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
