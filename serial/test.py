import flotilla
import time

c = flotilla.Client(port='/dev/ttyACM0')

try:
    while True:
        print(c.modules)
        time.sleep(1)
except KeyboardInterrupt:
    c.stop()
