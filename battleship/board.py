import numpy as np


class Board(object):
    __EMPTY = 0
    __GUESSED = 2

    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.area = np.full((rows, cols), self.__EMPTY, dtype=int)

    def place_ship(self, ship, pos):
        row, col = pos
        row_size, col_size = ship.area.shape
        row_limit, col_limit = (row + row_size), (col + col_size)
        try:
            if row >= self.rows or \
               col >= self.cols or \
               np.any(self.area[row:row_limit, col:col_limit] == ship.id):
                raise ValueError
            self.area[row:row_limit, col:col_limit] += ship.area
            return True
        except ValueError:
            print("Invalid ship location. Try again.")
            return False

    def update(self, pos):
        if self.area[pos] == self.__EMPTY:
            self.area[pos] = self.__GUESSED
            print('Miss.')
            return True
        elif self.area[pos] == self.__GUESSED:
            print('Already guessed that location. Try again.')
            return False
        else:
            self.area[pos] = self.__GUESSED
            print('Hit!')
            return True

    def has_remaining_ships(self, ship_id):
        return np.any(self.area != ship_id)
