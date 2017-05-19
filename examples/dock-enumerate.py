#!/usr/bin/env python

import time

import flotilla


print("""
This example will iterate through all connected Flotilla modules,
and list all connected devices and ports (unsorted).
""")

dock = flotilla.Client()

for module in dock.available.items():
    print(module)
print("")
dock.stop()
