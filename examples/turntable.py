#!/usr/bin/env python

# Script by Tanya Fish x

import sys
import time

import flotilla


#looks for the dock, and all of the modules we need attached to the dock so we can talk to them
dock = flotilla.Client()
motor = dock.first(flotilla.Motor)
touch = dock.first(flotilla.Touch)

current_offset=0
def go_to_offset(offset):
    target_offset=offset-current_offset
    motor.set_speed(target_offset)
    time.sleep(1)
    motor.stop()
    current_offset=target_offset

go_to_offset(10)
go_to_offset(-10)
