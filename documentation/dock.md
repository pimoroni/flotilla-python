## DOCK COMMANDS AND SETUP

For all Flotilla modules, you must import flotilla before using any of these commands.

Start your program with:

`import flotilla`

You will also need to make sure you are connected to the dock, and that it looks for the modules:

`dock = flotilla.Client()`

If you add in the following lines, it will wait until the dock is ready.

```python
while not dock.ready:
	pass
```

To connect to a module, you need to use:

```python
module = dock.first(flotilla.Module)
```

But please remember to change the word “module” or “Module” to the one you’re using! Eg.

```python
rainbow = dock.first(flotilla.Rainbow)
```

If you want to add more modules then just keep repeating the module line for each type you want to connect.*

You might want to add in an error message for if you’ve forgotten to plug in any of the modules, for example, if you’re using a Motor module you might write:

```python
if motor is None:
	print(“Motor module not plugged in. Try again!”)
	dock.stop()
	sys.exit(1)
else
	print(“Running…”)
```

*to connect more than one module of the same type, see advanced use.

## Advanced Commands

### Get all modules of a specific type

If you want to get all of the connected sliders, try:

```python
dock.all(flotilla.Slider)
```

### Get first, second or nth module of a specific type

To find the nth most module (in order from left to right) of a specific type connected to your dock you can use `first`, `second` or `nth` like so:

```python
dock.first(flotilla.Number) # Select the first connected number
dock.second(flotilla.Number) # Select the second connected number
dock.nth(flotilla.Slider, 3) # Select the third connected slider
```

### Check if you've got the right module back

Flotilla might return a `NoModule` object in cases where the right module is disconnected, or it might return a `Slider` when you expect a `Dial` if you request the module on a specific channel.

Check the modules are the ones you expect with `is_a`:

```python
my_module = dock.channel_four()
if my_module.is_a(flotilla.Slider):
    print("Slider found, value: {}".format(my_module.position))
else:
    print("Oh no, can't find the slider!")
```

This allows you to write code that responds to changes in the connected modules.

### Do something when a module is connected/disconnected

If you want to run some code when a module is connected or disconnected you can use `on_connect` and `on_disconnect` and pass them a function, like so:

```python
def handle_connect(channel, module):
    if module.is_a(flotilla.Joystick):
        print("Yay! You successfully connected a joystick!")

dock.on_connect(handle_connect)
```

Or using decorators:

```python
@dock.on_connect()
def handle_connect(channel, module):
    if module.is_a(flotilla.Slider):
        print("Good job! You connected a slider!")
```

