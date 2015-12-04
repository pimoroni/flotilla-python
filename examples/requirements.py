import flotilla
import time


client = flotilla.Client(
   requires={
        'one': flotilla.Touch,
	'eight': flotilla.Rainbow
    })

state = True

while not client.ready:
    pass

try:
    while True:
        state = not state
	
        time.sleep(1)
except KeyboardInterrupt:
    client.stop()

