## Colour module

The colour module has four light detectors in it: three of them have filters on to only let one colour of light in, and the fourth one lets all light in so can give you a light level.

First, don't forget to get the dock to recognise your module:

`colour = dock.first(flotilla.Colour)`

You can check how much light there is by looking at that fourth sensor and getting it to print the value it reads.

```python
print("The amount of light detected is...")
print(colour.clear)
```

In this example the detector takes all four readings and shows them on the screen every 10 seconds.
```python
import flotilla
import time

dock = flotilla.Client()
colour = dock.first(flotilla.Colour)

try:
  while True:
	print("The colours in clear, reg, green, blue order are:")
	print(colour.clear)
	print(colour.red)
	print(colour.green)
	print(colour.blue)
	time.sleep(10)

except KeyboardInterrupt:
	dock.stop()
```

*Colour summary*
*`colour.clear` - returns the value from the clear sensor (no filters)*
*`colour.red` - returns the value from the red sensor*
*`colour.green` - returns the value from the green sensor*
*`colour.blue` - returns the value from the blue sensor*


