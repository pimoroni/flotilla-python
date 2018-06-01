## Matrix module

The matrix module consists of 64 pixels arranged in an 8x8 grid.

First, don't forget to get the dock to recognise your module:

`matrix = dock.first(flotilla.Matrix)`

Each pixel on the matrix can be addressed by its X and Y position, both of these values range from 0 to 7 (that's 8 possible values).

A pixel can have a brightness between 0 (off) and 255 (fully on).

## Matrix summary

* `matrix.rotation(value)` - set the rotation of the matrix, either 0, 90, 180 or 270 degrees
* `matrix.set_brightness` - set the brightness of the matrix from 0 (off) to 255 (full)
* `matrix.set_pixel(x, y, brightness)` - set a single pixel on the matrix at x (0-7), y (0-7) with brightness (0-255)
* `matrix.update()` - display your changes on the matrix
* `matrix.clear()` - clear the matrix- you must call `update` for this to clear the display
