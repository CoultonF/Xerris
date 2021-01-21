from board import Board
from ship import Ship


class Player:
    def __init__(self, name):
        self.name = name
        self.ships = [Ship()]
        self.board = Board()
        self.victory = False
        self.defeat = False

    def attack(self, opponent, pos):
        repeat = opponent.defend(pos)
        while repeat:
            repeat = opponent.defend(pos)
        if not opponent.board.has_remaining_ships(self.ships[0].id()):
            self.victory = True

    def defend(self, pos):
        self.board.update(pos)
        if self.board.has_remaining_ships(self.ships[0].id()):
            self.defeat = True

    def place_ships(self, pos):
        for ship in self.ships:
            repeat = self.board.place_ship(ship, pos)
            while repeat:
                repeat = self.board.place_ship(ship, pos)
