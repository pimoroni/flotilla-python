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

## For Developers
If you need to modify the flotilla python library you can compile and test:
```bash
cd library
sudo ./setup.py build
sudo ./setup.py install
```
