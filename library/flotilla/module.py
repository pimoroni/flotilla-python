import time


class NoModule:
    def is_a(self, module_type):
        return isinstance(self, module_type)


class Module:
    name = None
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

    def __init__(self, channel, client):
        self.channel_index = channel
        self.client = client
        self.data = []

    def stop(self):
        pass

    def send(self, data):
        self.client.module_update(self.channel_index, ",".join([str(d) for d in data]))
        time.sleep(0.01)

    def set_data(self, data):
        changed = False
        if self.data != data:
            changed = True
        self.data = data
        return changed

    def is_a(self, module_type):
        return isinstance(self, module_type)

    def clamp(self, value, bounds_min, bounds_max):
        return max(min(value, bounds_max), bounds_min)

    @property
    def channel(self):
        return self._channel_names[self.channel_index]

