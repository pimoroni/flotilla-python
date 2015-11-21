import module


class Touch(module.Module):
    name = 'touch'

    @property
    def one(self):
        if len(self.data) >= 0:
            return int(self.data[0])
        return 0

    @property
    def two(self):
        if len(self.data) >= 2:
            return int(self.data[1])
        return 0

    @property
    def three(self):
        if len(self.data) >= 3:
            return int(self.data[2]) == 1
        return 0

    @property
    def four(self):
        if len(self.data) >= 4:
            return int(self.data[3]) == 1
        return 0
