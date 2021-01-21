from player import Player
from coordinates import Coordinates

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.coordinates = Coordinates()
        self.round = 0
        self.end = False
        self.start()

    def start(self):
        self.ship_placement(self.player1)
        self.ship_placement(self.player2)
        while not self.end():
            pass

    def is_end(self):
        if self.player1.victory:
            self.end = self.player1.victory and self.player2.defeat
            print('Player 1 wins.')
        if self.player2.victory:
            self.end = self.player2.victory and self.player1.defeat
            print('Player 2 wins.')

    def ship_placement(self, player):
        player.place_ships()