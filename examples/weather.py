#!/usr/bin/env python3

import time

import flotilla


print("""This example will read the temperature and pressure from any connected weather modules.

Press Ctrl+C to exit.""")


client = flotilla.Client()

try:
    while True:
        for module in client.available.values():
            if module.is_a(flotilla.Weather):
                print('Temp: {} Pressure: {}'.format(module.temperature, module.pressure))

        time.sleep(0.5)

except KeyboardInterrupt:
    client.stop()

