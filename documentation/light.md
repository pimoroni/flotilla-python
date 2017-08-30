## Light module

With the light sensor, you can sense light on two different scales.

First, don't forget to get the dock to recognise your module:

```python
light = dock.first(flotilla.Light)
```

Slightly confusingly, the light module returns the light level as `light.light` - the light level on the light module, so I like to rename it:

```python
lightlevel = light.light
```

If you wanted to show the light level on the screen you could write:

```python
lightlevel = light.light
print(lightlevel)
```

If you wanted to take a light reading every 3 seconds and display it with a little more panache:

```python
import flotilla
import time

dock = flotilla.Client()
light = dock.first(flotilla.Light)

try:
  while True:
    lightlevel = light.light
    print("The light level is currently...")
    print(lightlevel)
    time.sleep(3)

except KeyboardInterrupt:
  dock.stop()
```

It returns whole numbers only using these commands.
