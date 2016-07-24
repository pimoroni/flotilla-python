from .module import Module


class Slider(Module):
    name = 'slider'
    
    @property
    def position(self):
        if len(self.data) > 0:
             return int(self.data[0])
        return 0
