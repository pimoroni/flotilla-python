from .module import Module

class Matrix(Module):
    name = 'matrix'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.pixels = [0] * 8
        self.brightness = 40
        self.xstart = 7
        self.ystart = 7

    def rotation(self, r=0):
        if r == 0:
            self.xstart = 7
            self.ystart = 7
        elif r == 90:
            self.xstart = 0
            self.ystart = 7
        elif r == 180:
            self.xstart = 0
            self.ystart = 0
        elif r == 270:
            self.xstart = 7
            self.ystart = 0

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
