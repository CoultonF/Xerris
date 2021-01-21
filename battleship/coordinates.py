import string, re


class Coordinates:

    __ALPHABET_LEN = 26
    __OFFSET = 1

    def __init__(self):
        pass

    def alpha_index(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num = num * self.__ALPHABET_LEN + (ord(c.upper()) - ord('A')) + self.__OFFSET
        return num - self.__OFFSET

    def numeric_index(self, n):
        return int(n) - self.__OFFSET

    def split(self, coord):
        output = []
        m = None
        if coord[0].isdigit():
            m = next(re.finditer("[A-Za-z]+", coord))
        else:
            m = next(re.finditer("\d+", coord))
        output.append(coord[0:m.start()].upper())
        output.append(coord[m.start():m.end()].upper())
        output.sort()
        return output
