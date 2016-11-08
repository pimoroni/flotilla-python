#!/usr/bin/env python

from sys import version_info

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

    question0="Would you like to change the dock's identity? y/n "
    question1="What's your name? (8 characters max.) "
    question2="What name would you like to use for the dock? "

    if version_info[0] < 3:
        confirm = str(raw_input(question0))
        if confirm == "y":
            user = str(raw_input(question1))
            client.set_dock_user(user)
            name = str(raw_input(question2))
            client.set_dock_name(name)
        else:
            print("Bye!")
    elif version_info[0] == 3:
        confirm = str(input(question0))
        if confirm == "y":
            user = str(input(question1))
            client.set_dock_user(user)
            name = str(input(question2))
            client.set_dock_name(name)
        else:
            print("Bye!")
    print("")
    client.stop()
except AttributeError:
    print('''
    No dock found!
''')
