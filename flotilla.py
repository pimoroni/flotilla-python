import time
import threading
import websocket
import re
import signal
import atexit

class Dock():
    def __init__(self, version, serial, name, user):
        self.name = name
        self.user = user
        self.version = version
        self.serial = serial

class Module():
    name = 'module'
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

    def __init__(self, channel):
        self.channel_index = channel
        self.connected = False
        self.data = []
        self.host = 0

    def is_a(self, module_type):
        return isinstance(self, module_type)

    @property
    def channel(self):
        return self._channel_names[self.channel_index]

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def send(self, data):
        send("h:{} d:s {} {}".format(self.host,self.channel_index,data))

    def set_name(self, name):
        self.name = name

    def set_data(self, data):
        changed = False
        if self.data != data:
            changed = True
        self.data = data
        return changed

class Dial(Module):
    name = 'dial'

    @property
    def position(self):
        return int(self.data[0])

class Slider(Module):
    name = 'slider'

    @property
    def position(self):
        return int(self.data[0])

class Motion(Module):
    name = 'motion'

class Joystick(Module):
    name = 'joystick'

class Motor(Module):
    name = 'motor'

class Weather(Module):
    name = 'weather'

class Rainbow(Module): 
    name = 'rainbow'

    def set_rgb(self, r, g, b):
        self.send(",".join([str(r),str(g),str(b)] * 5))
    
    def set_rainbow(self, rainbow):
        self.send(",".join([str(x) for x in rainbow]))

class Light(Module):
    name = 'light'

class Touch(Module):
    name = 'touch'

class Colour(Module):
    name = 'colour'

class Matrix(Module):
    name = 'matrix'

    def __init__(self, channel):
        self.grid = [0] * 8
        self.brightness = 30
        Module.__init__(self, channel)

    def set_pixel(self, x, y, state):
        if state:
            self.grid[7-x] |= (1 << y)
        else:
            self.grid[7-x] &= ~(1 << y)

    def set_brightness(self, b):
        self.brightness = b

    def update(self):
        self.send("{pixels},{brightness}".format(
            pixels = ",".join([str(r) for r in self.grid]),
            brightness = self.brightness
        ))

    def clear(self):
        self.grid = [0] * 8

class Number(Module):
    name = 'number'

def module(channel_name):
    module_index = Module._channel_names.index(channel_name)
    return modules[module_index]

def all(module_type):
    return [module for module in modules if module is not None and  module.is_a(module_type)]

_ws = None
_ws_addr = "127.0.0.1"
_ws_port = 9395

_command_handlers = {}
dock = None
ready = False
running = False

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

supported_devices = _module_handlers.keys()

modules = [None for x in range(8)]

def _update_shortcuts():
    for channel_name in Module._channel_names:
        module_index = Module._channel_names.index(channel_name)
        globals()[channel_name] = modules[module_index]

def _create_new(channel, device_name):
    if device_name not in _module_handlers.keys():
        raise TypeError("{} not supported!".format(device_name))

    module = _module_handlers[device_name](channel)

    return module

def on_connect(handler=None):
    if handler is  None:
        def decorate(handler):
            global _on_connect
            _on_connect = handler
        return decorate
    else:
        _on_connect = handler

def on_disconnect(handler=None):
    if handler is None:
        def decorate(handler):
            global _on_disconnect
            _on_disconnect = handler
        return decorate
    else:
        _on_disconnect = handler

def on(device, handler=None):
    if type(device) is int:
        if device not in range(0,8):
            raise TypeError("Channel {channel} out of range!".format(channel=device))
    elif device not in _module_handlers.keys():
        raise TypeError("Device {device} not supported!".format(device=device))

    if handler is None:
        def decorate(handler):
            _command_handlers[device] = handler
        return decorate
    else:
         _command_handlers[device] = handler

def off(device):
    _command_handlers[device] = None

def on_message():
    pass

def on_update():
    pass

def _flotilla_on_ready():
    if "ready" in _command_handlers and callable(_command_handlers["ready"]):
        _ready_thread = threading.Thread(target= _command_handlers["ready"])
        _ready_thread.start()
   

def _flotilla_on_update():
    if "update" in _command_handlers and callable(_command_handlers["update"]):
        _command_handlers["update"]()

def _flotilla_on_command(channel, device, command, data):
    #print(channel, device, command, data)

    if command == "c":
        #print("Module connected: {} {}".format(device, channel))
        if modules[channel] is not None:
            return

        modules[channel] = _create_new(channel, device)
        _update_shortcuts()
        if callable(_on_connect):
            print("Calling connect handler")
            _on_connect(channel, modules[channel])
            #t = threading.Thread(_on_connect,args=(channel, modules[channel]))
            #t.start()
        return

    if command == "d":
        modules[channel].disconnect()
        
        if callable(_on_disconnect):
            print("Calling disconnect handler")
            _on_disconnect(channel, modules[channel])
            #t = threading.Thread(_on_disconnect,args=(channel, modules[channel]))
            #t.start()

        modules[channel] = None
        _update_shortcuts()
        return 
    
    if command == "u":
        if modules[channel].set_data(data):
            if channel in _command_handlers and callable(_command_handlers[channel]):
                _command_handlers[channel](modules[channel])
            if device in _command_handlers and callable(_command_handlers[device]):
                _command_handlers[device](modules[channel])
        return

def _ws_on_message(ws, message):
    global dock, ready
    #print(message)
    if message == 'update':
        _flotilla_on_update()
        return
    if message[0:8] == "# Dock: ":
        dock = message[8:].split(',')
        dock_version = dock[0]
        dock_serial  = dock[1]
        dock_name    = dock[2]
        dock_user    = dock[3]

        #print(message[8:])

        dock = Dock(dock_version, dock_serial, dock_name, dock_user)
        
        if not ready:
            send("ready")
            ready = True
            print("Sent ready status...")
        
        return
    
    if message[0] == '#':
        print('Debug: {}'.format(message))
        return

    packet = re.split('[$h|\ d]\:',message)[1:]
    host   = packet[0].strip()
    data   = packet[1].strip()

    if data[0] == '#':
        #print('Debug: {}'.format(data))
        return

    data = data.replace('  ',' ').replace('/',' ').replace(',',' ').split(' ')

    if(len(data) < 2):
        return

    command = data.pop(0).strip()
    channel = int(data.pop(0).strip())
    device  = data.pop(0).strip()

    _flotilla_on_command(channel, device, command, data)
     
def send(message):
    #print("Sending message", message)
    _ws.send(message)
       
def _ws_on_error(ws, error):
    print(error)

def _ws_on_close(ws):
    print('Closed!')

def _ws_on_open(ws):
    ws.send('hello')
    ws.send('ready')
    print('Open!')
    _flotilla_on_ready()

def _update():
    pass

def _ws_start():
    global _ws, _ws_addr, _ws_port

    #websocket.enableTrace(True)

    _ws = websocket.WebSocketApp("ws://{}:{}".format(_ws_addr, _ws_port),
                                on_message = _ws_on_message,
                                on_error   = _ws_on_error,
                                on_close   = _ws_on_close)
    _ws.on_open = _ws_on_open
    _ws.run_forever()        
    print("Websocket Stopped...")

def stop():
    global _ws, running
    _ws.close()
    running = False

def run(address=None, port=None):
    global _ws_addr, _ws_port, running
    
    if address is not None:
        _ws_addr = address
        
    if port is not None:
        _ws_port = port
    
    _thread = threading.Thread(target=_ws_start)
    _thread.start()
    
    running = True

def wait():
    signal.pause()

_on_connect = None
_on_disconnect = None

atexit.register(stop)
