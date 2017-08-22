## Motion module

The motion module has the ability to detect movement in 3d (steer), and the compass direction (heading).
First, don't forget to get the dock to recognise your module:

`motion = dock.first(flotilla.Motion)`

The motion module detects where it is using (x,y,z) coordinates, so side-side, up-down, front-back. 
You can check how far along the scale it is by asking it to show you the coordinate you want.
For example, to show you how far along the x-axis it is, 

```python
