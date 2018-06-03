# Flotilla Python API

This library interfaces with Flotilla over USB serial.

## Installing

We've created an installation script that will install the Flotilla python API and update your Dock in the process. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sS https://get.pimoroni.com/flotilla | bash
```

## IMPORTANT

If you've installed Rockpool, you need to shut down the Flotilla Daemon before you start talking to the dock using the present python API:

```bash
sudo service flotillad stop
```

## Generic python installing

Download or clone this repository and follow the instructions:

```bash
cd flotilla-python
pip install library
```

Now you'll be able to use Flotilla with python. Make sure your dock connected.

```python
>>> import flotilla
>>> dock = flotilla.Client()
>>> dock.ready
True
```
