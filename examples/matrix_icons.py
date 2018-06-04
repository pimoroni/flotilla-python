#!/usr/bin/env python

import sys
import time

import flotilla

print("""
This example will iterate through all connected Flotilla modules,
find each Matrix, and blink various versions of icons.

Press CTRL+C to exit.
""")

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
matrix = dock.first(flotilla.Matrix)

if matrix is None:
    print("no Matrix module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

try:

    matrix.full().update()
    time.sleep(1)

    matrix.clear().update()
    time.sleep(1)

    font = dict()
    font['first'] = 0x00040a1120408000
    font['letter-a'] = [0, 0, 0, 60, 96, 124, 102, 124]
    font['heart'] = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],

        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for p in font.values():
        print(matrix.set_matrix(p).update().pp())
        time.sleep(1)

    for p in font:
        print(matrix.set_icon(p, font).update().pp())
        time.sleep(1)

    for p in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890':
        print(matrix.set_icon(p).update().pp())
        time.sleep(1)

    print(matrix.set_icon("\\").update().pp())
    time.sleep(1)

    print(matrix.set_icon("%").update().pp())
    time.sleep(1)
    print(matrix.flip().update().pp())
    time.sleep(1)
    print(matrix.flip(horizontal=False).update().pp())
    time.sleep(1)

    print(matrix.set_icon("smiley").update().pp())
    time.sleep(1)

    for _ in range(10):
        print(matrix.invert().update().pp())
        print('')
        time.sleep(1)

    matrix.clear().update()

    print("Stopping Flotilla...")
    dock.stop()

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
