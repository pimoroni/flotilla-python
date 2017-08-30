## Joystick module

The joystick module has the ability to detect side to side movement of the stick (x), up and down movement of the stick (y), and a press of the button.

First, don't forget to get the dock to recognise your module:

`joystick = dock.first(flotilla.Joystick)`

The joystick detects where it is using (x,y) coordinates like you may have used in maths. 
You can check how far along the scale it is by asking it to show you the coordinate you want.
For example, to show you how far along the x-axis it is, 

```python
print("This is how far you are along the x-axis...")
print(joystick.x)
```

You should notice it only deals in positive whole numbers, where 0 is as far left as you can go, and 1023 is as far right as you can go.

You can similarly find out where it is on the y-axis by using `joystick.y`

```python
print("This is how far you are along the y-axis...")
print(joystick.y)
```

If you find out that the bottom left is NOT (0,0) then it could be that you're happier holding the joystick the other way around (the default numbers have the wire at the top).

If you want it to take readings with the wire at the bottom, add this line to the start of the program and it will change all the numbers for you.

```python
joystick.rotation(180)
```

Finally, if you press on the top of the joystick you'll hear a click. This is a simple button, and you can take the input from it as a 0 or 1, or as False or True.

```python
try:
	while True:
		if joystick.button:
			print ("BOOP")
```

This lets you print BOOP on the screen every time you click the button.

In this example the joystick says where it is on the coordinate grid every 5 seconds.

```python
import flotilla
import time

dock = flotilla.Client()

try:
	while True:
		print("You are holding the joystick at coordinates ({0}, {1})".format(joystick.x, joystick.y))
		time.sleep(5)

except KeyboardInterrupt:
	dock.stop()
```
