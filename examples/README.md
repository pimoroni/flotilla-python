# Flotilla Python Examples

These are basic examples for Flotilla controlled via Python.

## IMPORTANT 

If you've installed Rockpool, you need to shut down the Flotilla Daemon before you start talking to the dock using the present python API:

```bash
sudo service flotillad stop
```

identify.py
--------------

This is a simple script that will list the connected docks and provide info such as firmware version. Useful to check whether everything is up-to-date and otherwise hunky-dory!


blink-matrix.py
--------------

This example will iterate through all connected Flotilla modules,
find each Matrix, and blink one of the pixels.

It demonstrates how to find connected modules and identify a module by type.


mini-kit.py
------------

This example requires a Touch and Rainbow module (you'll find these in the mini kit):

Connect the Touch module on channel 1 on the dock.
Connect the Rainbow module on channel 8 on the dock.

Use the buttons on the Touch module to control your mood lighting as follows:

Button 1: change hue in one direction
Button 2: change hue in the other direction
Button 3: this button has no function
Button 4: switch Rainbow on and off


rainbow.py
--------------

This is a simple mood light example using Rainbow.


weather.py
--------------

Outputs the readings performed by the Weather module (Temperature/Pressure)
