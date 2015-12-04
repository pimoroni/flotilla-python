from .module import Module

class Rainbow(Module):
    name = 'rainbow'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.pixels = [(0, 0, 0)] * 5

    def set_pixel(self, x, r, g, b):
        self.pixels[x] = (r, g, b)

    def update(self):
        data = []
        for pixel in self.pixels:
            data += list(self.pixels[pixel])
        self.send(data)
