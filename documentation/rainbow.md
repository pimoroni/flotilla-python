## RAINBOW

In order to use your Rainbow, you'll need to make sure your dock recognizes it by adding the following line to your program:

```
rainbow = dock.first(flotilla.Rainbow)
```

With the Rainbow, you can address its pixels individually. Remember that numbering starts at zero, not one.

```python
rainbow.set_pixel(0, 255, 255, 255)

rainbow.update()
```

This example sets the first pixel (pixel 0) to a white light, and displays it.

You can set the colour of all of the pixels at once using

```python
rainbow.set_all(255, 255, 255)

rainbow.update()
```

The brightness is set globally by using a number from `0` (no light) to `255` (brightest).

```python
rainbow.set_brightness(100)
```

## Rainbow summary

* `set_pixel (pixel, red, green, blue)` - address individual pixels
* `set_all (red, green, blue)` - address all pixels
* `set_brightness(brightness)` - set brightness using numbers from 0-255
* `update()` - shows the pixels
* `stop()` - clears all pixels
