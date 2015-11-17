import flotilla
import time

@flotilla.on(5)
def channel_5(module):
    if module.is_a(flotilla.Dial):
        print(module.position)

flotilla.run()

while flotilla.running:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        flotilla.stop()
        exit()
