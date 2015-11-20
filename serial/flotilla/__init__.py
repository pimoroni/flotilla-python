import threading
import re
import serial
import atexit

from dial import Dial
from slider import Slider
#from motion import Motion
#from number import Number
from matrix import Matrix

class Client:
    _module_handlers = {
        'dial': Dial,
        'slider': Slider,
        #'motion': Motion,
        'matrix': Matrix,
        #'number': Number,
        #'touch': Touch,
        #'light': Light,
        #'colour': Colour,
        #'joystick': Joystick,
        #'motor': Motor,
        #'weather': Weather,
        #'rainbow': Rainbow
    }

    def __init__(self, port='/dev/ttyACM0', baud=9600):
        self.num_channels = 8
        self.port = port
        self.baud = baud
        self.running = True
        self.modules = [None] * self.num_channels


        self._on_connect = None
        self._on_disconnect = None

        self.serial = serial.Serial(port, baud, timeout=0)

        self._thread = threading.Thread(target=self._poll_serial)
        self._thread.start()
        atexit.register(self.stop)

        self.serial.write("\r")
        self.serial.flush()
        self.serial.write("e\r")
        self.serial.flush()

    @property
    def supported_modules(self):
        return self._module_handlers.keys()

    def _handle_command(self, command):
        print(command)

        if command[0:8] == "# Dock: ":
            dock =  command[8:].split(",")
            dock_version = dock[0]
            dock_serial = dock[1]
            dock_name = dock[2]
            dock_user = dock[3]
            return

        if command[0] == "#":
            self._debug(command)
            return

        data = command.replace('  ',' ').replace('/', ' ').replace(',',' ').split(' ')

        if len(data) < 2:
            # Invalid Packet
            return

        command = data.pop(0).strip()
        channel = int(data.pop(0).strip())
        device = data.pop(0).strip()

        self._handle_module_command(channel, device, command, data)

    def _handle_module_command(self, channel, device, command, data):
        if command == "u":
            if self.modules[channel] is not None:
                self.modules[channel].set_data(data)
            return

        if command == "c":
            if self.modules[channel] is None:
                self.modules[channel] = self._new_module(channel, device)
                if callable(self._on_connect):
                    self._on_connect(channel, self.modules[channel])
            return

        if command == "d":
            if self.modules[channel] is not None:
                if callable(self._on_disconnect):
                    self._on_disconnect(channel, self.modules[channel])
                self.modules[channel] = None
            return
    
    def _new_module(self, channel, device_name):
        if device_name not in self.supported_modules:
            raise TypeError("Module {} not supported!".format(device_name))

        return self._module_handlers[device_name](channel)


    def on_connect(self, handler=None):
        if handler is  None:
            def decorate(handler):
                self._on_connect = handler
            return decorate
        else:
            self._on_connect = handler

    def on_disconnect(self, handler=None):
        if handler is None:
            def decorate(handler):
                self._on_disconnect = handler
            return decorate
        else:
            self._on_disconnect = handler

    def on(device, handler=None):
        pass

    def _poll_serial(self):
        command = ""
        while self.running:
            character = self.serial.read(1).decode()

            if character == "\n":
                c = threading.Thread(target=self._handle_command, args=(command,))
                c.start()
                command = ""
                continue

            if character:
                command += character
    
    def stop(self):
        self.running = False

    def __del__(self):
        self.stop()
