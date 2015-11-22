import flotilla
import time


client = flotilla.Client(
    port='/dev/tty.usbmodem1411',
    requires={
        'four': flotilla.Matrix,
        'seven': flotilla.Matrix,
        'five': flotilla.Number,
        'three': flotilla.Joystick,
        'six': flotilla.Motor
    })

state = True

while not client.ready:
    pass

try:
    while True:
        state = not state
        client.channel_four.set_pixel(0, 0, state).set_pixel(7, 7, state).update()
        client.channel_seven.set_pixel(0, 0, state).set_pixel(7, 7, state).update()
        time.sleep(1)
except KeyboardInterrupt:
    client.stop()

