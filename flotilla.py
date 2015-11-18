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
    def __init__(self, channel, name):
        self.channel = channel
        self.name = name
        self.connected = False
        self.data = []
        self.host = 0

    def is_a(self, module_type):
        return isinstance(self, module_type)

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def send(self, data):
        send("h:{} d:s {} {}".format(self.host,self.channel,data))

    def set_name(self, name):
        self.name = name

    def set_data(self, data):
        changed = False
        if self.data != data:
            changed = True
        self.data = data
        return changed

class Dial(Module):
    def __init__(self, channel):
        Module.__init__(self, channel, 'dial')

    @property
    def position(self):
        return int(self.data[0])

class Slider(Module):
    def __init__(self, channel):
        Module.__init__(self, channel, 'slider')

    @property
    def position(self):
        return int(self.data[0])

class Motion(Module):
    pass

class Joystick(Module):
    pass

class Motor(Module):
    pass

class Weather(Module):
    pass

class Rainbow(Module): 
    def set_rgb(self, r, g, b):
        self.send(",".join([str(r),str(g),str(b)] * 5))
    
    def set_rainbow(self, rainbow):
        self.send(",".join([str(x) for x in rainbow]))

class Light(Module):
    pass

class Touch(Module):
    def __init__(self, channel):
        Module.__init__(self, channel, 'touch')

class Colour(Module):
    pass

class Matrix(Module):
    pass

class Number(Module):
    pass

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

def _create_new(channel, device_name):
    if device_name not in _module_handlers.keys():
        raise TypeError("{} not supported!".format(device_name))

    module = _module_handlers[device_name](channel)

    return module

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
        modules[channel] = _create_new(channel, device)
        return

    if command == "d":
        modules[channel].disconnect()
        modules[channel] = None
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
    atexit.register(stop)

def wait():
    signal.pause()
