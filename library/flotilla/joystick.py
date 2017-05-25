from .module import Module

class Joystick(Module):
    name = 'joystick'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.xstart = 1023
        self.ystart = 1023

    def rotation(self, r=0):
        if r == 0:
            self.xstart = 1023
            self.ystart = 1023
        elif r == 180:
            self.xstart = 0
            self.ystart = 0

    @property
    def button(self):
        if len(self.data) > 0:
            return int(self.data[0]) == 1
        return 0

    @property
    def x(self):
        if len(self.data) > 1:
            return abs(_xstart - int(self.data[1]))
        return 0

    @property
    def y(self):
        if len(self.data) > 2:
            return abs(_ystart - int(self.data[2]))
        return 0
