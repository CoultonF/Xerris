import numpy as np


class Ship:

    __ID = 1

    def __init__(self, rows=3, cols=1):
        self.area = np.full((rows, cols), self.__ID, dtype=int)

    def rotate(self):
        self.area = self.area.T

    def id(self):
        return self.__ID
