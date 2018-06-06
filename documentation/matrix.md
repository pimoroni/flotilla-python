## Matrix module

The matrix module consists of 64 pixels arranged in an 8x8 grid.

First, don't forget to get the dock to recognise your module:

`matrix = dock.first(flotilla.Matrix)`

Each pixel on the matrix can be addressed by its X and Y position, both of these values range from 0 to 7 (that's 8 possible values).

A pixel can have a brightness between 0 (off) and 255 (fully on).

## Matrix summary

* `matrix.rotation(value)` - set the rotation of the matrix, either 0, 90, 180 or 270 degrees
* `matrix.set_brightness` - set the brightness of the matrix from 0 (off) to 255 (full)
* `matrix.set_pixel(x, y, state)` - set a single pixel on the matrix at x (0-7), y (0-7) with state 0 (off) or 1 (on)
* `matrix.update()` - display your changes on the matrix
* `matrix.clear()` - clear the matrix- you must call `update` for this to clear the display


## Matrix advanced features

* `matrix.invert()` - invert all pixel states
* `matrix.full()` - invert `clear`
* `matrix.flip(value)` - flips pixels horizontal if `True` (default) or vertical if `False`
* `matrix.set_matrix('0x00040a1120408000')` - set display full matrix as hex in one call


    pix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],

    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]

* `matrix.set_matrix(pix)` - set display full matrix as nested list of bits in one call
* `matrix.set_matrix([0, 0, 0, 60, 96, 124, 102, 124])` - set display full matrix as list of int in one call
* `matrix.set_icon('A')` - set predefined icon from ascii font
* `matrix.set_icon(key, font)` - set custom icon (`matrix.set_matrix` input) as provided by `font`
* `matrix.pp()` - pretty print of display pixel
