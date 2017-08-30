## Dial module

The dial module has a potentiometer and 5 LED lights to show you where you are on the scale.

First, don't forget to get the dock to recognise your module:

`dial = dock.first(flotilla.Dial)`

You can show where the dial is on a scale of 0-1023 by using the following code:

```python
print("The dial is at position...")
print(dial.position)
```

In this example if the dial is above halfway (512) then it prints the word "LOUD", if it's below halfway it prints the word "quiet".

```python
import flotilla
import time

dock = flotilla.Client()
slider = dock.first(flotilla.Dial)

try:
  while True:
	pos = int(dial.position)
	if pos > 512:
		print("LOUD")
	if 0 < pos < 512:
		print("quiet")
	time.sleep(1)

except KeyboardInterrupt:
	dock.stop()
```

You can use the dial to control other modules by using `dial.position` as an input variable, although you might want to rename it something shorter like in the example above.

## Dial Summary

* `dial.position` - returns dial position between 0-1023


