from .module import Module


class Motor(Module):
    name = 'motor'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.speed = 0

    def update(self):
        self.send([self.speed])

    def stop(self):
        self.speed = 0
        self.update()

    def speed(self, speed):
        self.speed = self.clamp(speed, -63, 63)
        self.update()
