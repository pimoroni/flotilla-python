from .module import Module

_xstart = 7
_ystart = 7

class Matrix(Module):
    name = 'matrix'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.pixels = [0] * 8
        self.brightness = 40

    def rotation(self, r=0):
        global _xstart
        global _ystart
        if r == 0:
            _xstart = 7
            _ystart = 7
        elif r == 90:
            _xstart = 0
            _ystart = 7
        elif r == 180:
            _xstart = 0
            _ystart = 0
        elif r == 270:
            _xstart = 7
            _ystart = 0

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_pixel(self, x, y, state):
        if state:
            self.pixels[abs(_xstart-x)] |= (1 << abs(_ystart-y))
        else:
            self.pixels[abs(_xstart-x)] &= ~(1 << abs(_ystart-y))
        return self

    def update(self):
        self.send(self.pixels + [self.brightness])

    def clear(self):
        self.pixels = [0] * 8
        return self
