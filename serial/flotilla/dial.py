import module

class Dial(module.Module):
    name = 'dial'
    
    @property
    def position(self):
        if len(self.data) > 0:
             return int(self.data[0])
        return 0
