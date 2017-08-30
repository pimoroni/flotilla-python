## Touch module

The touch module has 4 capacitative touch buttons.
First, don't forget to get the dock to recognise your module:

`touch = dock.first(flotilla.Touch)`

The buttons are numbered 1-4 on the actual module, and you address each of them by using their number.

```python
if touch.one:
	print("Button 1 pressed!")
```

You can address the other three buttons in the same way. Here is an example using all four buttons as a quote generator.

```python
import flotilla

dock = flotilla.Client()
touch = dock.first(flotilla.Touch)

try:
  while True:
	if touch.one:
		print("Your mother smells of elderberries")
	if touch.two:
		print("Your father was a hamster")
	if touch.three:
		print("He's a Very Naughty Boy")
	if touch.four:
		print("Blue or Yellow?")

except KeyboardInterrupt:
	dock.stop()
```

## Touch summary

* `if touch.one:` - looks for button 1 being pressed
* `if touch.two:` - looks for button 2 being pressed
* `if touch.three:` - looks for button 3 being pressed
* `if touch.four:` - looks for button 4 being pressed
