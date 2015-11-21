import threading
import re
import serial
import atexit
import time

from .module import Module
from .dial import Dial
from .slider import Slider
from .motion import Motion
from .number import Number
from .matrix import Matrix
from .joystick import Joystick


class Client:
    _module_handlers = {
        'dial': Dial,
        'slider': Slider,
        'motion': Motion,
        'matrix': Matrix,
        'number': Number,
        # 'touch': Touch,
        # 'light': Light,
        # 'colour': Colour,
        'joystick': Joystick,
        # 'motor': Motor,
        # 'weather': Weather,
        # 'rainbow': Rainbow
    }

    def __init__(self, port='/dev/tty.usbmodem1431', baud=9600):
        self.num_channels = 8
        self.port = port
        self.baud = baud
        self.running = True
        self.modules = [Module(x, self) for x in range(self.num_channels)]

        self.dock_name = None
        self.dock_user = None
        self.dock_serial = None
        self.dock_version = None

        self._on_connect = None
        self._on_disconnect = None

        self.serial = serial.Serial(port, baud, timeout=0)

        self._thread = threading.Thread(target=self._poll_serial)
        self._thread.start()
        atexit.register(self.stop)

        self.request_version_info()

        time.sleep(0.5)
        self.enumerate_devices()

    def _serial_write(self, data):
        self.serial.write(bytes(data + "\r", "ascii"))

    def set_dock_name(self, name):
        name = name[0:8]
        self._serial_write("n d {}".format(name))

    def set_dock_user(self, user):
        user = user[0:8]
        self._serial_write("n u {}".format(user))

    def request_version_info(self):
        self._serial_write("v")

    def enumerate_devices(self):
        self._serial_write("e")

    def module_update(self, channel_index, data):
        self._serial_write("s {} {}".format(channel_index, data))

    @property
    def supported_modules(self):
        return self._module_handlers.keys()

    def _handle_command(self, command):
        print(command)
        command = command.strip()

        if command[0] == "#":
            if command[0:8] == "# Dock: ":
                self.dock_name = command[8:]
            elif command[0:8] == "# User: ":
                self.dock_user = command[8:]
            elif command[0:11] == "# Version: ":
                self.dock_version = command[10:]
            elif command[0:10] == "# Serial: ":
                self.dock_serial = command[10:]

            self._debug(command)

            return

        data = command.replace('  ', ' ').replace('/', ' ').replace(',', ' ').split(' ')

        if len(data) < 2:
            # Invalid Packet
            return

        command = data.pop(0).strip()
        channel = int(data.pop(0).strip())
        device = data.pop(0).strip()

        self._handle_module_command(channel, device, command, data)

    def _debug(self, command):
        print("Debug: {}".format(command))

    def _handle_module_command(self, channel, device, command, data):
        if command == "u":
            if not self.modules[channel].is_a(Module):
                self.modules[channel].set_data(data)
            return

        if command == "c":
            if self.modules[channel].is_a(Module):
                self.modules[channel] = self._new_module(channel, device)
                if callable(self._on_connect):
                    self._on_connect(channel, self.modules[channel])
            return

        if command == "d":
            if not self.modules[channel].is_a(Module):
                if callable(self._on_disconnect):
                    self._on_disconnect(channel, self.modules[channel])
                self.modules[channel] = None
            return

    def _new_module(self, channel, device_name):
        if device_name not in self.supported_modules:
            raise TypeError("Module {} not supported!".format(device_name))

        return self._module_handlers[device_name](channel, self)

    def on_connect(self, handler=None):
        if handler is None:
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

    def on(self, device, handler=None):
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
