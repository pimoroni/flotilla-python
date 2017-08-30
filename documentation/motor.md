## Motor module

With the motor, you can control the speed and the direction. Remember to get the dock to recognise it by adding

`motor = dock.first(flotilla.Motor)`

You can set the speed to anything between 1 (slowest forwards) and 63 (fastest forwards) like this:

```python
motor.set_speed(20)
motor.update()
```

This sets the speed to 20 and then turns it on. You can stop the motor by setting the speed to zero or by using

`motor.stop()`

For example, if I wanted the motor to go at about half speed forwards for 5 seconds, and then stop, I would write:

```python
motor.set_speed(32)
motor.update()
time.sleep(5)
motor.stop()
```

Don't forget to `import time` if you are going to use waiting times and so on.

To make the motor go backwards, just use the speed in a negative direction.

```python
motor.set_speed(-20)
motor.update()
```

This would make the motor go at speed 20 in the opposite direction.

There are some examples of controlling a motor with other flotilla modules in the flotilla examples directory.

## Motor summary

* motor.set_speed() = set the running speed of the motor
* motor.update() = set the motor running
* motor.stop() = sets the speed to zero and updates