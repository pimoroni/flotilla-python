#!/usr/bin/env python3

import colorsys
import time
import flotilla

print("Stop this script using ctrl-c")

# Set required connections - following video
client = flotilla.Client(
    requires={
        'two': flotilla.Rainbow,
        'three': flotilla.Matrix,
        'four': flotilla.Light,
        'five': flotilla.Light,
        'six': flotilla.Motor,
        'seven': flotilla.Motor
    }
)

# Wait for client
while not client.ready:
    pass

# Create local variables for every component
colours = {
    'red':  [255,0,0,600],
    'green':[0,255,0,500],
    'blue': [0,0,255,1100],
    'white': [255,255,255,1400  ]
}
rainbow = client.channel_two
matrix = client.channel_three
light_right = client.channel_four
light_left = client.channel_five
motor_left = client.channel_six
motor_right = client.channel_seven

# Set variables following the pimoroni sample

_current_colour = 'white'
_forward_speed = 30
_threshold = .6



try:
    _active_color = colours[_current_colour]
    rainbow.set_all(
        _active_color[0],
        _active_color[1],
        _active_color[2]
    )
    rainbow.update()
    while True:

        motor_left.stop()
        motor_right.stop()

        level_left = light_left.light / _active_color[3]
        level_right = light_right.light / _active_color[3]

        scale_left = -((abs(level_left) -.07) * 3.33)
        scale_right = (abs(level_right) -.07) * 3.33

        # Information for debugging
        print("{0:.2f}, {1:.2f} --- {2:.2f},{3:.2f} ::  {4:.2f},{5:.2f}".format(
            level_left,
            level_right,
            scale_left,
            scale_right,
            (_forward_speed * scale_left),
            (_forward_speed * scale_right)
        ))


        if level_left > _threshold:
            motor_left.speed = _forward_speed * scale_left
        if level_right > _threshold:
            motor_right.speed = _forward_speed * scale_right

        motor_left.update()
        motor_right.update()


        time.sleep(0.05)

except KeyboardInterrupt:
    motor_left.stop()
    motor_right.stop()
    rainbow.stop()
    client.stop()
