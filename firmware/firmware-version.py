#!/usr/bin/env python3

import flotilla

try:
    client = flotilla.Client()
    print('''Flotilla Dock Found:
Version: {dock_version}'''.format(dock_version=client.dock_version))
    client.stop()
except AttributeError:
    print('Firmware version unreadable')
