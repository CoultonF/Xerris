import string
import re


class Coordinates:
    __ALPHABET_LEN = 26
    __OFFSET = 1

    def __init__(self):
        pass

    def get_pos(self):
        coord = self.split(str(input('Enter coordinates like A1: ')))
        return self.numeric_index(coord[0]), self.alpha_index(coord[1])

    def alpha_index(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num = num * self.__ALPHABET_LEN + (ord(c.upper()) - ord('A')) + self.__OFFSET
        return num - self.__OFFSET

    def numeric_index(self, n):
        return int(n) - self.__OFFSET

    def split(self, coord):
        # clean the input to only alphanumeric as
        # python arrays have negative number logic.
        pattern = re.compile(r'[\W_]+')
        coord = pattern.sub('', coord)

        output = []
        m = None
        try:
            if coord[0].isdigit():
                m = next(re.finditer(r'[A-Za-z]+', coord))
            else:
                m = next(re.finditer(r'\d+', coord))
        except StopIteration:
            # 0A is considered an invalid position.
            return '0A'
        output.append(coord[0:m.start()].upper())
        output.append(coord[m.start():m.end()].upper())
        output.sort()
        return output
