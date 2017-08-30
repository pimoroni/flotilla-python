## Weather module

With the weather sensor, you can sense temperature in degrees centigrade, and air pressure in hPa.
First, don't forget to get the dock to recognise your module:

`weather = dock.first(flotilla.Weather)`

If you wanted to show the current temperature in degrees Centigrade on the screen you could write:

```python
print(weather.temperature)
```

If you wanted to take a reading every 3 seconds and display it with a little more panache:

```python
import flotilla
import time

dock = flotilla.Client()
weather = dock.first(flotilla.Weather)

try:
  while True:
    print("The temperature is currently...")
    print(weather.temperature)
    time.sleep(3)

except KeyboardInterrupt:
  dock.stop()
```

You can do the same sort of thing with the pressure reading:

```python
print(weather.pressure)
```

## Weather summary

* `weather.temperature` - reads the temperature in C
* `weather.pressure` - reads the air pressure (divide by 10 for hPa, multiply by 10 for Pa)

It returns whole numbers only using these commands.
