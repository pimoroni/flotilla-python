from .module import Module


class Motor(Module):
    name = 'motor'

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self._speed = 0

    def update(self):
        self.send([self._speed])

    def stop(self):
        self._speed = 0
        self.update()

    def reverse(self):
        self._speed = -self._speed
        self.update()

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
	    self.set_speed(speed)
		
    def set_speed(self, speed):
        self._speed = self.clamp(_speed, -63, 63)
        self.update()
