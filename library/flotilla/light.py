from .module import Module


class Light(Module):
    name = 'light'

    @property
    def light(self):
        if len(self.data) > 0:
            return int(self.data[0])
        return 0

    @property
    def lux(self):
        if len(self.data) > 2:
            return int(self.data[2])
        return 0
