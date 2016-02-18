from .module import Module


class Weather(Module):
    name = 'weather'

    @property
    def pressure(self):
        if len(self.data) >= 0:
            return int(self.data[1]) / 10
        return 0

    @property
    def temperature(self):
        if len(self.data) >= 0:
            return float(self.data[0]) / 100
        return 0