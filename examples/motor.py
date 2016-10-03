#!/usr/bin/env python3
import time
import flotilla

print("""
This example uses 2 motors and increase the speed every second
Easy to upgrade to use buttons or as a base for line following robot
Stop this script using ctrl-c
""")

# Set required connections - following video
client = flotilla.Client(
    requires={
        'six': flotilla.Motor,
        'seven': flotilla.Motor
    }
)

# Wait for client
while not client.ready:
    pass

motor_left = client.channel_six
motor_right = client.channel_seven

# Set variables following the pimoroni sample
speed = 0

try:
    while True:
        speed +=5
        motor_left.speed = -speed
        motor_right.speed = speed

        motor_left.update()
        motor_right.update()
        print("Current speed: {0}".format(speed))

        time.sleep(1)

except KeyboardInterrupt:
    motor_left.stop()
    motor_right.stop()
    client.stop()
