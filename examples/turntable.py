#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
motor = dock.first(flotilla.Motor)
touch = dock.first(flotilla.Touch)

if motor is None or touch is None:
    print("modules required not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

current_offset=0

def go_to_offset(offset):
    target_offset=offset-current_offset
    motor.set_speed(target_offset)
    time.sleep(1)
    motor.stop()
    current_offset=target_offset

go_to_offset(10)
go_to_offset(-10)
