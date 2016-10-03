#!/usr/bin/env python3

import flotilla


try:
    client = flotilla.Client()

    print('''
    Flotilla Dock Found:

        User:    {dock_user}
        Name:    {dock_name}
        Version: {dock_version}
        Serial:  {dock_serial}
'''.format(
            dock_version=client.dock_version,
            dock_user=client.dock_user,
            dock_name=client.dock_name,
            dock_serial=client.dock_serial
        ))

    client.stop()
except AttributeError:
    print('''
    No dock found!
''')

