import time
import threading
import websocket
import re
import signal

_ws = None
_command_handlers = {}
dock = None

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

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def set_rgb(self, r, g, b):
        self.send(",".join([str(r),str(g),str(b)] * 5))
    
    def set_rainbow(self, rainbow):
        self.send(",".join([str(x) for x in rainbow]))

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

modules = [Module(x,'none') for x in range(8)]

def on(device, handler=None):
    if handler is None:
        def decorate(handler):
            _command_handlers[device] = handler
        return decorate
    else:
        _command_handlers[device] = handler

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
        print("Module connected: {} {}".format(device, channel))
        modules[channel].connect()
        modules[channel].set_name(device)
        return

    if command == "d":
        modules[channel].disconnect()
        return 
    
    if command == "u":
        if modules[channel].set_data(data):
            if device in _command_handlers and callable(_command_handlers[device]):
                _command_handlers[device](data)
        return

def _ws_on_message(ws, message):
    global dock
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

        print(message[8:])

        dock = Dock(dock_version, dock_serial, dock_name, dock_user)
        send("ready")
        print("Sent ready status...")
        return
    if message[0] == '#':
        print('Debug: {}'.format(message))
        return

    packet = re.split('[$h|\ d]\:',message)[1:]
    host   = packet[0].strip()
    data   = packet[1].strip()

    if data[0] == '#':
        print('Debug: {}'.format(data))
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
    global _ws

    #websocket.enableTrace(True)

    _ws = websocket.WebSocketApp("ws://127.0.0.1:9393",
                                on_message = _ws_on_message,
                                on_error   = _ws_on_error,
                                on_close   = _ws_on_close)
    _ws.on_open = _ws_on_open
    _ws.run_forever()        

def run():
    _thread = threading.Thread(target=_ws_start)
    _thread.start()

def wait():
    signal.pause()
