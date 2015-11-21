from .module import Module


class Joystick(Module):
    name = 'joystick'

    @property
    def x(self):
        if len(self.data) >= 2:
            return int(self.data[1])
        return 0

    @property
    def y(self):
        if len(self.data) >= 3:
            return int(self.data[2])
        return 0

    @property
    def button(self):
        if len(self.data) >= 0:
            return int(self.data[0]) == 1
        return 0
