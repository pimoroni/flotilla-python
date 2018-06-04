from .module import Module

try:
    x = long(1)
except:
    long = int

class Matrix(Module):
    name = 'matrix'
    _font = {
        'A': [0, 60, 102, 102, 126, 102, 102, 102],
        'B': [0, 62, 102, 102, 62, 102, 102, 62],
        'C': [0, 60, 102, 6, 6, 6, 102, 60],
        'D': [0, 62, 102, 102, 102, 102, 102, 62],
        'E': [0, 126, 6, 6, 62, 6, 6, 126],
        'F': [0, 126, 6, 6, 62, 6, 6, 6],
        'G': [0, 60, 102, 6, 6, 118, 102, 60],
        'H': [0, 102, 102, 102, 126, 102, 102, 102],
        'I': [0, 60, 24, 24, 24, 24, 24, 60],
        'J': [0, 120, 48, 48, 48, 54, 54, 28],
        'K': [0, 102, 54, 30, 14, 30, 54, 102],
        'L': [0, 6, 6, 6, 6, 6, 6, 126],
        'M': [0, 198, 238, 254, 214, 198, 198, 198],
        'N': [0, 198, 206, 222, 246, 230, 198, 198],
        'O': [0, 60, 102, 102, 102, 102, 102, 60],
        'P': [0, 62, 102, 102, 102, 62, 6, 6],
        'Q': [0, 60, 102, 102, 102, 118, 60, 96],
        'R': [0, 62, 102, 102, 62, 30, 54, 102],
        'S': [0, 60, 102, 6, 60, 96, 102, 60],
        'T': [0, 126, 90, 24, 24, 24, 24, 24],
        'U': [0, 102, 102, 102, 102, 102, 102, 124],
        'V': [0, 102, 102, 102, 102, 102, 60, 24],
        'W': [0, 198, 198, 198, 214, 254, 238, 198],
        'X': [0, 198, 198, 108, 56, 108, 198, 198],
        'Y': [0, 102, 102, 102, 60, 24, 24, 24],
        'Z': [0, 126, 96, 48, 24, 12, 6, 126],
        'a': [0, 0, 0, 60, 96, 124, 102, 124],
        'b': [0, 6, 6, 6, 62, 102, 102, 62],
        'c': [0, 0, 0, 60, 102, 6, 102, 60],
        'd': [0, 96, 96, 96, 124, 102, 102, 124],
        'e': [0, 0, 0, 60, 102, 126, 6, 60],
        'f': [0, 56, 108, 12, 12, 62, 12, 12],
        'g': [0, 0, 124, 102, 102, 124, 96, 60],
        'h': [0, 6, 6, 6, 62, 102, 102, 102],
        'i': [0, 0, 24, 0, 24, 24, 24, 60],
        'j': [0, 48, 0, 48, 48, 54, 54, 28],
        'k': [0, 6, 6, 102, 54, 30, 54, 102],
        'l': [0, 24, 24, 24, 24, 24, 24, 24],
        'm': [0, 0, 0, 198, 238, 254, 214, 214],
        'n': [0, 0, 0, 62, 126, 102, 102, 102],
        'o': [0, 0, 0, 60, 102, 102, 102, 60],
        'p': [0, 0, 62, 102, 102, 62, 6, 6],
        'q': [0, 0, 60, 54, 54, 60, 176, 240],
        'r': [0, 0, 0, 62, 102, 102, 6, 6],
        's': [0, 0, 0, 124, 2, 60, 64, 62],
        't': [0, 0, 24, 24, 126, 24, 24, 24],
        'u': [0, 0, 0, 102, 102, 102, 102, 124],
        'v': [0, 0, 0, 0, 102, 102, 60, 24],
        'w': [0, 0, 0, 198, 214, 214, 214, 124],
        'x': [0, 0, 0, 102, 60, 24, 60, 102],
        'y': [0, 0, 0, 102, 102, 124, 96, 60],
        'z': [0, 0, 0, 60, 48, 24, 12, 60],
        '1': [0, 24, 24, 28, 24, 24, 24, 126],
        '2': [0, 60, 102, 96, 48, 12, 6, 126],
        '3': [0, 60, 102, 96, 56, 96, 102, 60],
        '4': [0, 48, 56, 52, 50, 126, 48, 48],
        '5': [0, 126, 6, 62, 96, 96, 102, 60],
        '6': [0, 60, 102, 6, 62, 102, 102, 60],
        '7': [0, 126, 102, 48, 48, 24, 24, 24],
        '8': [0, 60, 102, 102, 60, 102, 102, 60],
        '9': [0, 60, 102, 102, 124, 96, 102, 60],
        '0': [0, 60, 102, 118, 110, 102, 102, 60],
        '!': [0, 24, 60, 60, 24, 24, 0, 24],
        '"': [0, 108, 108, 40, 0, 0, 0, 0],
        '#': [0, 108, 108, 254, 108, 254, 108, 108],
        '$': [0, 16, 120, 4, 56, 64, 60, 16],
        '%': [0, 6, 102, 48, 24, 12, 102, 96],
        '&': [0, 60, 102, 60, 20, 166, 102, 252],
        "'": [0, 24, 24, 24, 12, 0, 0, 0],
        '(': [0, 96, 48, 24, 24, 24, 48, 96],
        ')': [0, 6, 12, 24, 24, 24, 12, 6],
        '*': [0, 0, 108, 56, 254, 56, 108, 0],
        '+': [0, 0, 16, 16, 124, 16, 16, 0],
        ',': [0, 0, 0, 0, 12, 12, 12, 6],
        '-': [0, 0, 0, 0, 60, 0, 0, 0],
        '.': [0, 0, 0, 0, 0, 0, 6, 6],
        '/': [0, 0, 96, 48, 24, 12, 6, 0],
        ':': [0, 0, 24, 24, 0, 24, 24, 0],
        ';': [0, 0, 24, 24, 0, 24, 24, 12],
        '<': [0, 96, 48, 24, 12, 24, 48, 96],
        '=': [0, 0, 0, 60, 0, 60, 0, 0],
        '>': [0, 6, 12, 24, 48, 24, 12, 6],
        '?': [0, 60, 102, 96, 56, 24, 0, 24],
        '@': [0, 28, 34, 58, 26, 66, 60, 0],
        '[': [0, 120, 24, 24, 24, 24, 24, 120],
        "\\": [0, 0, 6, 12, 24, 48, 96, 0],
        ']': [0, 30, 24, 24, 24, 24, 24, 30],
        '^': [0, 16, 40, 68, 130, 0, 0, 0],
        '_': [0, 0, 0, 0, 0, 0, 0, 255],
        '`': [0, 48, 48, 96, 0, 0, 0, 0],
        '{': [0, 112, 24, 24, 12, 24, 24, 112],
        '|': [24, 24, 24, 24, 24, 24, 24, 24],
        '}': [0, 14, 24, 24, 48, 24, 24, 14],
        '~': [0, 0, 0, 92, 54, 0, 0, 0],
        'smiley': [126, 129, 165, 129, 189, 153, 129, 126],
        'heard': [0, 108, 254, 254, 124, 56, 16, 0]
    }

    def __init__(self, channel, client):
        Module.__init__(self, channel, client)
        self.pixels = [0] * 8
        self.brightness = 40
        self.xstart = 7
        self.ystart = 7

    def rotation(self, r=0):
        if r == 0:
            self.xstart = 7
            self.ystart = 7
        elif r == 90:
            self.xstart = 0
            self.ystart = 7
        elif r == 180:
            self.xstart = 0
            self.ystart = 0
        elif r == 270:
            self.xstart = 7
            self.ystart = 0
        return self

    def set_brightness(self, brightness):
        self.brightness = brightness
        return self

    def set_pixel(self, x, y, state):
        if state:
            self.pixels[abs(self.xstart - x)] |= (1 << abs(self.ystart - y))
        else:
            self.pixels[abs(self.xstart - x)] &= ~(1 << abs(self.ystart - y))
        return self

    def update(self):
        self.send(self.pixels + [self.brightness])
        return self

    def clear(self):
        self.pixels = [0] * 8
        return self

    def full(self):
        self.clear().invert()
        return self

    def invert(self):
        self.pixels = list(255 - x for x in self.pixels)
        return self

    def flip(self, horizontal=True):
        if horizontal:
            self.pixels = list(
                Matrix._int_from_bit_list(list(reversed(Matrix._int_to_bit_list(x)))) for x in self.pixels)
        else:
            self.pixels = list(reversed(self.pixels))
        return self

    @property
    def matrix(self):
        return list(self._int_to_bit_list(i) for i in self.pixels)

    @matrix.setter
    def matrix(self, matrix):
        self.set_matrix(matrix)

    def set_matrix(self, matrix, base=2):
        if isinstance(matrix, str):
            # matrix defines self.pixels as a str repr of a single int
            matrix = int(matrix, base=base)
        if isinstance(matrix, (int, long)):
            # matrix defines self.pixels as a single int
            matrix = self._pixels_from_int(matrix)
        if all(isinstance(x, (int, long)) for x in matrix):
            # matrix is, as expected, a list of ints
            self.pixels = matrix
        elif all(isinstance(x, str) for x in matrix):
            # matrix is list of str, each str repr an int
            self.pixels = [int(m, base=base) for m in matrix]
        elif all(isinstance(x, (list, tuple)) for x in matrix):
            # matrix is a list of bit list, which defines a single pixel
            self.pixels = [self._int_from_bit_list(m) for m in matrix]
        else:
            raise TypeError('Matrix cannot handle %s input.' % matrix.__class__.__name__)
        return self

    @staticmethod
    def _int_to_bit_list(integer):
        return list(int(x) for x in list('{0:08b}'.format(integer)))

    @staticmethod
    def _int_from_bit_list(bits):
        d = len(bits) - 1
        return sum(pow(2, d - i) for i, x in enumerate(bits) if int(x))

    @staticmethod
    def _pixels_from_int(integer):
        bits = '{0:064b}'.format(integer)
        bits = tuple(bits[8 * i:8 * (i + 1)] for i in range(8))
        pixels = list()
        for b in bits:
            pixels.append(int(b, base=2))
        return pixels

    @staticmethod
    def _pixels_to_int(pixels):
        m = list(Matrix._int_to_bit_list(i) for i in pixels)
        int_list = list()
        for bits in m:
            int_list.extend(bits)
        return Matrix._int_from_bit_list(int_list)

    def set_icon(self, icon, font={}):
        i = self._font.get(str(icon), [0] * 8)
        i = font.get(icon, i)
        self.set_matrix(i)
        return self

    def pp(self, sep='\n'):
        s = list()
        for line in self.matrix:
            s.append(''.join('*' if b else ' ' for b in reversed(line)))
        return sep.join(s)
