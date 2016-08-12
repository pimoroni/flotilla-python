# -*- coding: utf-8 -*-
import time
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
    _font = [
        0,                                                              # (space)
        0,                                                              # !      
        NUM_TR,                                                         # "      
        0,                                                              # #      
        0,                                                              # $      
        0,                                                              # %      
        0,                                                              # &      
        NUM_TL,                                                         # '      
        NUM_TL + NUM_BL + NUM_B + NUM_T,                                # (      
        NUM_B + NUM_BR + NUM_TR + NUM_T,                                # )      
        0,                                                              # *      
        0,                                                              # +      
        NUM_DOT,                                                        # ,      
        NUM_MID,                                                        # -      
        NUM_DOT,                                                        # .      
        NUM_BL + NUM_TR,                                                # /      
        NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_TR + NUM_T,              # 0      
        NUM_BR + NUM_TR,                                                # 1      
        NUM_MID + NUM_BL + NUM_B + NUM_TR + NUM_T,                      # 2      
        NUM_MID + NUM_B + NUM_BR + NUM_TR + NUM_T,                      # 3      
        NUM_MID + NUM_TL + NUM_BR + NUM_TR,                             # 4      
        NUM_MID + NUM_TL + NUM_B + NUM_BR + NUM_T,                      # 5      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_T,             # 6      
        NUM_TL + NUM_BR + NUM_TR + NUM_T,                               # 7      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_TR + NUM_T,    # 8      
        NUM_MID + NUM_TL + NUM_B + NUM_BR + NUM_TR + NUM_T,             # 9      
        0,                                                              # :      
        0,                                                              # ;      
        NUM_BL + NUM_B,                                                 # <      
        NUM_MID + NUM_B,                                                # =      
        NUM_B + NUM_BR,                                                 # >      
        NUM_MID + NUM_BL + NUM_TR + NUM_T,                              # ?      
        NUM_MID + NUM_BL + NUM_B + NUM_BR + NUM_TR + NUM_T,             # @      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR + NUM_TR + NUM_T,            # A      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_BR,                     # B      
        NUM_MID + NUM_BL + NUM_B,                                       # C      
        NUM_MID + NUM_BL + NUM_B + NUM_BR + NUM_TR,                     # D      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_T,                      # E      
        NUM_MID + NUM_TL + NUM_BL + NUM_T,                              # F      
        NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_T,                       # G      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR,                             # H      
        NUM_BR,                                                         # I      
        NUM_BL + NUM_B + NUM_BR + NUM_TR,                               # J      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR + NUM_T,                     # K      
        NUM_TL + NUM_BL + NUM_B,                                        # L      
        NUM_TL + NUM_BL + NUM_BR + NUM_TR + NUM_T,                      # M      
        NUM_MID + NUM_BL + NUM_BR,                                      # N      
        NUM_MID + NUM_BL + NUM_B + NUM_BR,                              # O      
        NUM_MID + NUM_TL + NUM_BL + NUM_TR + NUM_T,                     # P      
        NUM_MID + NUM_TL + NUM_BR + NUM_TR + NUM_T,                     # Q      
        NUM_MID + NUM_BL,                                               # R      
        NUM_MID + NUM_TL + NUM_B + NUM_BR,                              # S      
        NUM_MID + NUM_TL + NUM_BL + NUM_B,                              # T      
        NUM_BL + NUM_B + NUM_BR,                                        # U      
        NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_TR,                      # V      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_TR,            # W      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR + NUM_TR,                    # X      
        NUM_MID + NUM_TL + NUM_B + NUM_BR + NUM_TR,                     # Y      
        NUM_BL + NUM_B + NUM_TR + NUM_T,                                # Z      
        NUM_TL + NUM_BL + NUM_B + NUM_T,                                # [      
        NUM_TL + NUM_BR,                                                # "\"    
        NUM_B + NUM_BR + NUM_TR + NUM_T,                                # ]      
        NUM_T,                                                          # ^      
        NUM_B,                                                          # _      
        NUM_TL,                                                         # `      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR + NUM_TR + NUM_T,            # a      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_BR,                     # b      
        NUM_MID + NUM_BL + NUM_B,                                       # c      
        NUM_MID + NUM_BL + NUM_B + NUM_BR + NUM_TR,                     # d      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_T,                      # e      
        NUM_MID + NUM_TL + NUM_BL + NUM_T,                              # f      
        NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_T,                       # g      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR,                             # h      
        NUM_BR,                                                         # i      
        NUM_BL + NUM_B + NUM_BR + NUM_TR,                               # j      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR + NUM_T,                     # k      
        NUM_TL + NUM_BL + NUM_B,                                        # l      
        NUM_TL + NUM_BL + NUM_BR + NUM_TR + NUM_T,                      # m      
        NUM_MID + NUM_BL + NUM_BR,                                      # n      
        NUM_MID + NUM_BL + NUM_B + NUM_BR,                              # o      
        NUM_MID + NUM_TL + NUM_BL + NUM_TR + NUM_T,                     # p      
        NUM_MID + NUM_TL + NUM_BR + NUM_TR + NUM_T,                     # q      
        NUM_MID + NUM_BL,                                               # r      
        NUM_MID + NUM_TL + NUM_B + NUM_BR,                              # s      
        NUM_MID + NUM_TL + NUM_BL + NUM_B,                              # t      
        NUM_BL + NUM_B + NUM_BR,                                        # u      
        NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_TR,                      # v      
        NUM_MID + NUM_TL + NUM_BL + NUM_B + NUM_BR + NUM_TR,            # w      
        NUM_MID + NUM_TL + NUM_BL + NUM_BR + NUM_TR,                    # x      
        NUM_MID + NUM_TL + NUM_B + NUM_BR + NUM_TR,                     # y      
        NUM_BL + NUM_B + NUM_TR + NUM_T,                                # z      
        NUM_MID + NUM_BR + NUM_TR,                                      # {      
        NUM_TL + NUM_BL,                                                # |      
        NUM_MID + NUM_TL + NUM_BL,                                      # }
        NUM_MID + NUM_TL + NUM_TR + NUM_T,                              # ° (~)      
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

    def set_colon(self, value):
        if value < 0 or value > 1:
            raise ValueError("Unsupported value for colon")

        self.colon = value

    def set_apostrophe(self, value):
        if value < 0 or value > 1:
            raise ValueError("Unsupported value for apostrophe")

        self.apostrophe = value

    def set_brightness(self, value):
        if value < 0 or value > 255:
            raise ValueError("Unsupported value for brightness")

        self.brightness = value

    def set_string(self, string):
        if type(string) is not str:
            raise TypeError("You should pass a string as a parameter")

        self.set_colon(0)        
        dots = [".", ","]
        digit = 0

        for x in range(len(string)):
            if digit > 3:
                continue

            char = string[x]
            if char  in dots:
                if x == 0 or string[x - 1]  in dots:
                    self.set_char(digit, char, 0)
                    digit += 1
                else:
                    self.set_char(digit - 1, string[x - 1], 1)
            elif char == ":" and digit == 2:
                self.set_colon(1)
            else: 
                self.set_char(digit, char, 0)
                digit += 1

    def set_char(self, digit, value, dot=0):
        if 0 > digit > 3:
            raise ValueError("Digit must be between 0 and 3")

        char = self._get_char(value)
        self.digits[digit] = char + dot

    def set_temp(self, value):
        temp = 0
        try:
            temp = float(value)
        except ValueError:
            raise TypeError("Value must be a number") 

        if temp >= 999.5 or temp < -99.5:
            self.set_string("Err")
            # raise ValueError("Number is too big: %d" % number)
        else:
            int_len = len(str(int(temp // 1)))
            width = 4 - int_len // 3
            precission = 3 - int_len 
            self.set_string("{:{}.{}f}~".format(temp, width, precission))

    def set_current_time(self, colon=1):
        self.set_string(time.strftime("%H%M"))
        if colon < 0 or colon > 1:
            raise ValueError("Unsupported value for colon")
        self.set_colon(colon)

    def _get_char(self, char):
        char_ordinal = None

        try:
            char_ordinal = ord(char) - 32
        except TypeError:
            pass

        if char_ordinal is None or char_ordinal > len(self._font):
            raise ValueError("Unsupported char {}".for_mat(char))

        return self._font[char_ordinal]

