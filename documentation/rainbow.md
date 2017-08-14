## RAINBOW

The first thing about the Rainbow is that you can address the pixels individually. 
Remember that numbering starts at zero, not one.



```

rainbow.set_pixel(0, 255, 255, 255)

rainbow.update()

```


This example sets the first pixel (pixel 0) to a white light, and displays it.


You can set the colour of all of the pixels at once using



```

rainbow.set_all(255, 255, 255)

rainbow.update()

```


You can also set the brightness of the pixels by adding a fifth parameter in the brackets, for example:



```

rainbow.set_pixel(2, 255, 0, 255, 0.5)

rainbow.update()

```



Would set the third pixel (pixel 2) to magenta at half brightness. 
The value for brightness should be between 0.0 (dark) and 1.0 (full brightness). 
It can be used in combination with the set all function, for example



```

rainbow.set_all (255, 255, 0, 1)

rainbow.update()

```



Would set all the pixels to yellow at full brightness.


You can set the brightness globally by using



`rainbow.set_brightness(0.5)`



which would set all pixels to half brightness for the remainder of the program.




*Rainbow summary:
*
*`set_pixel (red, green, blue, brightness)` - address individual pixels*

*`set_all (red, green, blue, brightness)` - address all pixels*

*`clear_all ()` - sets all pixels to off*

*`update()` - shows the pixels*