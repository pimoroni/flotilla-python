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

    def send(self, data):
        self.client.module_update(self.channel_index, ",".join([str(d) for d in data]))

    def set_data(self, data):
        changed = False
        if self.data != data:
            changed = True
        self.data = data
        return changed

    def is_a(self, module_type):
        return isinstance(self, module_type)


    @property
    def channel(self):
        return self._channel_names[self.channel_index]
    
