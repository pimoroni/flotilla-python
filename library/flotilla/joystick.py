from .module import Module

_xstart = 1023
_ystart = 1023

class Joystick(Module):
    name = 'joystick'

    def rotation(self, r=0):
        global _rotation
        global _xstart
        global _ystart
        if r == 0:
            _xstart = 1023
            _ystart = 1023
        elif r == 180:
            _xstart = 0
            _ystart = 0

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
