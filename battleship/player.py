from battleship.board import Board
from battleship.ship import Ship
from battleship.coordinates import Coordinates


class Player:
    def __init__(self):
        self.ships = [Ship()]
        self.board = Board()
        self.coordinates = Coordinates()
        self.victory = False

    def attack(self, opponent):
        pos = self.coordinates.get_pos()
        success = opponent.board.update(pos)
        while not success:
            pos = self.coordinates.get_pos()
            success = opponent.board.update(pos)
        if not opponent.board.has_remaining_ships(self.ships[0].id()):
            self.victory = True

    def play_ships(self):
        print('Your ship:\n', self.ships[0].area)
        rotate = input('Rotate ship?(y/n) ') == 'y'
        if rotate:
            self.ships[0].rotate()
            print("Rotated. \n", self.ships[0].area)
        pos = self.coordinates.get_pos()
        placed = self.board.place_ship(self.ships[0], pos)
        while not placed:
            pos = self.coordinates.get_pos()
            placed = self.board.place_ship(self.ships[0], pos)
        return True

