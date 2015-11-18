#!/usr/bin/env python

import flotilla
import time

def handle_everything(module):
    if module.is_a(flotilla.Dial):
        print(module.position)

for device in flotilla.supported_devices:
    print("Handling {device}".format(device=device))
    flotilla.on(device, handle_everything)

flotilla.run()

while flotilla.running:
    try:
        print("Hello World")
        time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping Flotilla...")
        flotilla.stop()
