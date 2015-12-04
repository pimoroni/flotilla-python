#!/usr/bin/env python

import flotilla
import time

def handle_everything(module):
    if module.is_a(flotilla.Dial):
        print(module.position)
        x = int((module.position/1023.0) * 7.0)
        print(x)
        for matrix in flotilla.all(flotilla.Matrix):
            matrix.clear()
            matrix.set_pixel(x,0,1)
            matrix.update()

for device in flotilla.supported_devices:
    print("Handling {device}".format(device=device))
    flotilla.on(device, handle_everything)

@flotilla.on_connect()
def connect(channel, module):
    if module.is_a(flotilla.Dial):
        for matrix in flotilla.all(flotilla.Matrix):
            matrix.clear()
            matrix.set_pixel(0,0,1)
            matrix.update()

    if module.is_a(flotilla.Matrix):
        print("Matrix connected!!!")
        module.clear()
        for x in range(8):
            for y in range(8):
                module.set_pixel(x,y,1)
        module.update()

@flotilla.on_disconnect()
def disconnect(channel, module):
    pass

flotilla.run()

while flotilla.running:
    try:
        print("Hello World")
        time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping Flotilla...")
        flotilla.stop()
