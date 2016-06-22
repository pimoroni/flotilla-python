from .module import Module

class Touch(Module):
    name = 'touch'

    @property
    def one(self):
        if len(self.data) > 0:
            return int(self.data[0]) == 1
        return False

    @property
    def two(self):
        if len(self.data) > 1:
            return int(self.data[1]) == 1
        return False

    @property
    def three(self):
        if len(self.data) > 2:
            return int(self.data[2]) == 1
        return False

    @property
    def four(self):
        if len(self.data) > 3:
            return int(self.data[3]) == 1
        return False
