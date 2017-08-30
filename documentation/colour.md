## Colour module

The colour module has four light detectors: three of them have filters that only let in one colour of light (red, green or blue), the fourth lets in all light to give you an overall light level.

First, don't forget to get the dock to recognise your module:

`colour = dock.first(flotilla.Colour)`

You can check how much light there is by looking at that fourth sensor and printing its value.

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

## Colour summary

* `colour.clear` - returns the value from the clear sensor (no filters)
* `colour.red` - returns the value from the red sensor
* `colour.green` - returns the value from the green sensor
* `colour.blue` - returns the value from the blue sensor


