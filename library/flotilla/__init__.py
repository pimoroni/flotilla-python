import threading
import re
import serial
import serial.tools.list_ports
import atexit
import time
import sys
from subprocess import check_output, CalledProcessError

from .module import Module, NoModule
from .dial import Dial
from .slider import Slider
from .motion import Motion
from .number import Number
from .matrix import Matrix
from .joystick import Joystick
from .motor import Motor
from .touch import Touch
from .rainbow import Rainbow
from .light import Light
from .weather import Weather
from .colour import Colour

VID = 0x16d0
PID = 0x08c3

LANG_REQUIRES = "Oh no! I need a {module_type} on channel {channel}"
LANG_FOUND = "Yay! I've found a {module_type} on channel {channel}"
LANG_READY = "Everything connected properly. Let's go!"

class Client:
    _module_handlers = {
        'dial': Dial,
        'slider': Slider,
        'motion': Motion,
        'matrix': Matrix,
        'number': Number,
        'touch': Touch,
        'light': Light,
        'colour': Colour,
        'joystick': Joystick,
        'motor': Motor,
        'weather': Weather,
        'rainbow': Rainbow
    }
    _channel_names = [
        'eight',
        'seven',
        'six',
        'five',
        'four',
        'three',
        'two',
        'one'
    ]

    def __init__(self, port=None, baud=115200, requires=None, debug=False, clear_on_exit=True):
        self._enable_debug = debug
        self.clear_state_on_exit = clear_on_exit

        self.running = False

        self.dock_name = None
        self.dock_user = None
        self.dock_serial = None
        self.dock_version = None

        self._on_connect = None
        self._on_disconnect = None

        self.num_channels = 8
        self.port = port
        self.baud = baud

        self._modules = [NoModule() for x in range(self.num_channels)]

        self.ready = False
        self.module_changed = None

        self._requires = requires

        # Sniff for a running Flotilla Server instance and error if found
        self._check_flotilla_server()

        # Try to find the port automagically if it's not supplied
        if self.port is None:
            self.port = self._find_serial_port()

        self.serial = serial.Serial(self.port, self.baud, timeout=0)

        self._start()

    def _start(self):
        self.running = True
        self._thread = threading.Thread(target=self._poll_serial)
        self._thread.start()
        atexit.register(self.stop)

        self._wait_for_version_info()

        self.enumerate_devices()

        time.sleep(0.5) # Allow enough time for enumeration to complete

        self._check_requirements_and_launch_loop()

        self.ready = True

    def _find_serial_port(self):
        ports = serial.tools.list_ports.comports()

        for check_port in ports:
            if hasattr(serial.tools,'list_ports_common'):
                if (check_port.vid, check_port.pid) == (VID, PID):
                    return check_port.device
                continue
            if "USB VID:PID={vid}:{pid}".format(vid=hex(VID)[2:].upper(),pid=hex(PID)[2:].upper()) in check_port[2].upper():
                return check_port[0]

        raise AttributeError("Couldn't find Flotilla. Please try specifying a port.")

    def _check_flotilla_server(self):
        try:
            pid = check_output(["pidof","flotilla"]).strip()
            pid = int(pid)
        except (CalledProcessError, OSError):
            pid = 0

        if pid > 0:
            raise AttributeError("""Flotilla server is running!
Please stop it before using the Python API.
Try: kill {pid}""".format(pid=pid))

    def _request_version_info(self):
        self._serial_write("v")

    def _wait_for_version_info(self):
        while None in (self.dock_name, self.dock_user, self.dock_serial, self.dock_version):
            self._request_version_info()
            time.sleep(1)

    def _check_requirements_and_launch_loop(self):
        if self._requires is None:
            return

        if not self._required_modules_connected():
            for channel in self._requires.keys():
                module_type = self._requires[channel]
                channel_index = self._channel_names.index(channel)

                if not self._modules[channel_index].is_a(module_type):
                    print(LANG_REQUIRES.format(
                        module_type=module_type.name,
                        channel=channel
                    ))
                else:
                    print(LANG_FOUND.format(
                        module_type=module_type.name,
                        channel=channel
                    ))

            while not self._required_modules_connected():
                time.sleep(0.5)
        print(LANG_READY)

    def _required_modules_connected(self):
        if self._requires is not None:
            for channel in self._requires.keys():
                module_type = self._requires[channel]
                channel_index = self._channel_names.index(channel)
                if not self._modules[channel_index].is_a(module_type):
                    return False

        return True

    def _serial_write(self, data):
        self._debug("Sending: {}".format(data))
        
        try:
            data = bytes(data + "\r", "ascii")
        except TypeError:
            data = bytes(data + "\r")

        self.serial.write(data)

    def set_dock_name(self, name):
        '''Update the saved dock name in dock EEPROM
        
        Arguments:
            @name - The dock name to set, max 8 chars
        '''
        name = name[0:8]
        self._serial_write("n d {}".format(name))

    def set_dock_user(self, user):
        '''Update the saved user name in dock EEPROM

        Arguments:
            @user - The user name to set, max 8 chars
        '''
        user = user[0:8]
        self._serial_write("n u {}".format(user))

    def request_version_info(self):
        self._serial_write("v")

    def enumerate_devices(self):
        '''Request a list of connected devices from the dock
        '''
        self._serial_write("e")

    def module_update(self, channel_index, data):
        if self.dock_version > 0.1:
            channel_index = self._channel_index_to_number(channel_index)
        self._serial_write("s {} {}".format(channel_index, data))

    def first(self, type):
        for module in self.available.values():
            if module.is_a(type):
                return module

    @property
    def channel_one(self):
        return self._modules[self._channel_names.index('one')]

    @property
    def channel_two(self):
        return self._modules[self._channel_names.index('two')]

    @property
    def channel_three(self):
        return self._modules[self._channel_names.index('three')]

    @property
    def channel_four(self):
        return self._modules[self._channel_names.index('four')]

    @property
    def channel_five(self):
        return self._modules[self._channel_names.index('five')]

    @property
    def channel_six(self):
        return self._modules[self._channel_names.index('six')]

    @property
    def channel_seven(self):
        return self._modules[self._channel_names.index('seven')]

    @property
    def channel_eight(self):
        return self._modules[self._channel_names.index('eight')]

    @property
    def available(self):
        modules = {}
        for x in range(8):
            if self._modules[x].is_a(Module):
                modules[self._channel_names[x]] = self._modules[x]
        return modules

    @property
    def supported_modules(self):
        return self._module_handlers.keys()

    def _handle_command(self, command):
        self._debug("Command: {}".format(command))

        command = command.strip()
        
        if len(command) == 0:
            return

        if command[0] == "#":
            if command[0:8] == "# Dock: ":
                self.dock_name = command[8:]

            elif command[0:8] == "# User: ":
                self.dock_user = command[8:]

            elif command[0:11] == "# Version: ":
                self.dock_version = float(command[10:])

            elif command[0:10] == "# Serial: ":
                self.dock_serial = command[10:]

            self._debug(command)

            return

        if self.dock_version is None:
            return

        data = command.replace('  ', ' ').replace('/', ' ').replace(',', ' ').split(' ')

        if len(data) < 2:
            # Invalid Packet
            return

        command = data.pop(0).strip()
        channel = int(data.pop(0).strip())
        if self.dock_version > 0.1:
            channel_index = self._channel_number_to_index(channel)
            self._debug("Converting channel from {} to {}".format(channel, channel_index))
            channel = channel_index

        device = data.pop(0).strip()

        self._handle_module_command(channel, device, command, data)

    def _debug(self, command):
        if not self._enable_debug:
            return
        print("Debug: {}".format(command))

    def _channel_number_to_index(self, channel_number):
        return [-1,7,6,5,4,3,2,1,0][channel_number]

    def _channel_index_to_number(self, channel_index):
        return [8,7,6,5,4,3,2,1][channel_index]

    def _handle_module_command(self, channel, device, command, data):
        if command == "u":
            if not self._modules[channel].is_a(NoModule):
                if self._modules[channel].set_data(data):
                    if callable(self.module_changed):
                        self.module_changed(self._channel_names[channel],self._modules[channel])
            return

        if command == "c":
            if self._modules[channel].is_a(NoModule):
                self._modules[channel] = self._new_module(channel, device)
                self._debug("Found module: {}".format(device))
                if callable(self._on_connect):
                    self._on_connect(channel, self._modules[channel])
            return

        if command == "d":
            if not self._modules[channel].is_a(NoModule):
                self._debug("Lost module: {}".format(device))
                if callable(self._on_disconnect):
                    self._on_disconnect(channel, self._modules[channel])
                self._modules[channel] = NoModule()
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
        if not self.running:
            return

        if self.clear_state_on_exit:
            for module in self.available.values():
                module.stop()

        self.running = False

    def __del__(self):
        self.stop()
