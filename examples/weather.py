#!/usr/bin/env python

print("""This example will read the temperature and pressure from any connected weather modules.

Press Ctrl+C to exit.""")

import flotilla
import time

client = flotilla.Client()

try:
    while True:
        for module in client.available.values():
            if module.is_a(flotilla.Weather):
                print('Temp: {} Pressure: {}'.format(module.temperature, module.pressure))

        time.sleep(0.5)

except KeyboardInterrupt:
    client.stop()

