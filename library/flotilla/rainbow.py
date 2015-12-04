from .module import Module

class Rainbow(Module):
    name = 'rainbow'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.num_pixels = 5
        self.pixels = [(0, 0, 0)] * self.num_pixels
        self.brightness = 150

    def set_pixel(self, x, r, g, b):
        self.pixels[x] = (r, g, b)
        return self

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_all(self, r, g, b):
        for x in range(self.num_pixels):
            self.set_pixel(x, r, g, b)        
        return self

    def update(self):
        data = []
        for pixel in self.pixels:
            data += list(pixel)
        self.send(data)
