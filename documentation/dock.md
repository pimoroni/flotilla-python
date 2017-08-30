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
