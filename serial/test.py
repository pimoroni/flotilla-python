import flotilla
import time

c = flotilla.Client(port='/dev/tty.usbmodem1431')

state = True

try:
    while True:
        print(c.modules)

        if c.modules[2] is not None and c.modules[2].is_a(flotilla.Matrix):
            c.modules[2].set_pixel(1, 1, state).update()
            state = not state

        time.sleep(1)
except KeyboardInterrupt:
    c.stop()
