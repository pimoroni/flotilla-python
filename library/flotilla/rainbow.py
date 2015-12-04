import module


class Rainbow(module.Module):
    name = 'rainbow'

    def __init__(self, channel):
        module.Module.__init__(self, channel)
        self.pixels = [(0, 0, 0)] * 5

    def set_pixel(self, x, r, g, b):
        self.pixels[x] = (r, g, b)

    def update(self):
        data = []
        for pixel in self.pixels:
            data += list(self.pixels[pixel])
        self.send(data)
