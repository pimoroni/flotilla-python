## Slider module

The slider module has a sliding potentiometer and 5 LED lights to show you where you are on the scale.
First, don't forget to get the dock to recognise your module:

`slider = dock.first(flotilla.Slider)`

You can show where the slider is on a scale of 0-1023 by using the following:

```python
print("The slider is at position...")
print(slider.position)
```

In this example if the slider is above halfway (512) then it prints the word BIG, if it's below halfway it prints the word SMALL.

```python
import flotilla
import time

dock = flotilla.Client()
slider = dock.first(flotilla.Slider)

try:
  while True:
	pos = int(slider.position)
	if pos > 512:
		print("BIG")
	if 0 < pos < 512:
		print("SMALL")
	time.sleep(1)

except KeyboardInterrupt:
	dock.stop()
```

You can use the slider to control other modules by using `slider.position` as an input variable, although you might want to rename it something shorter like in the example above.

## Slider summary

* `slider.position` - returns slider position between 0-1023


