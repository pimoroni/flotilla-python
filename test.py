#!/usr/bin/env python

import flotilla
import time

def handle_everything(channel, device, data):
    print(channel, device, data)

for device in flotilla.supported_devices:
    print("Handling {}".format(device=device))
    flotilla.on(device, handle_everything)

flotilla.run()

while flotilla.running:
    try:
        print("Hello World")
        time.sleep(1)
    except KeyboardInterrupt:
        flotilla.stop()
