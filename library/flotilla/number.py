from .module import Module

NUM_DOT = 1
NUM_MID = 2
NUM_TL = 4
NUM_BL = 8
NUM_B = 16
NUM_BR = 32
NUM_TR = 64
NUM_T = 128

"""
0 = Digit 1
1 = Digit 2
2 = Digit 3
3 = Digit 4
4 = 1/0 colon
5 = 1/0 apostrophe
6 = brightness
"""


class Number(Module):
    name = 'number'
    _numbers = [
        NUM_TL + NUM_BL + NUM_T + NUM_B + NUM_TR + NUM_BR,
        NUM_TR + NUM_BR,
        NUM_BL + NUM_T + NUM_B + NUM_TR + NUM_MID,
        NUM_T + NUM_B + NUM_TR + NUM_BR + NUM_MID,
        NUM_TR + NUM_TL + NUM_MID + NUM_BR,
        NUM_TL + NUM_BR + NUM_MID + NUM_T + NUM_B,
        NUM_T + NUM_MID + NUM_B + NUM_BL + NUM_BR + NUM_TL,
        NUM_T + NUM_TR + NUM_BR,
        NUM_TL + NUM_BL + NUM_T + NUM_B + NUM_TR + NUM_BR + NUM_MID,
        NUM_TL + NUM_T + NUM_TR + NUM_BR + NUM_MID
    ]

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.digits = [0] * 4
        self.brightness = 40

        self.colon = 0
        self.apostrophe = 0

    def set_number(self, number):
        if type(number) is not int:
            raise TypeError("Number must be an integer")
        if number > 9999:
            raise ValueError("Number is too big: %d" % number)
        if number < 0:
            raise ValueError("Number must not be negative: %d" % number)

        number = [int(x) for x in "%04d" % number]
        for x in range(len(number)):
            self.set_digit(x, number[x])

    def set_digit(self, digit, value):
        if 0 > value > 9:
            raise ValueError("Value must between 0 and 9")
        if 0 > digit > 3:
            raise ValueError("Digit must be between 0 and 3")

        self.digits[digit] = self._numbers[value]

    def update(self):
        self.send(self.digits + [self.colon, self.apostrophe, self.brightness])

    def clear(self):
        self.digits = [0] * 4
        return self
