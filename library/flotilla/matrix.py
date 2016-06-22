from .module import Module


class Matrix(Module):
    name = 'matrix'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.pixels = [0] * 8
        self.brightness = 40

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_pixel(self, x, y, state):
        if state:
            self.pixels[7-x] |= (1 << y)
        else:
            self.pixels[7-x] &= ~(1 << y)
        return self

    def update(self):
        self.send(self.pixels + [self.brightness])

    def clear(self):
        self.pixels = [0] * 8
        return self
