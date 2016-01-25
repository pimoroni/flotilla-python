from .module import Module


class Light(Module):
    name = 'light'

    @property
    def light(self):
        if len(self.data) >= 0:
            return int(self.data[0])
        return 0
