from battleship.player import Player

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.round = 1

    def play(self):
        print('\nRound %d - place ships.' % self.round)
        print('Player 1\'s turn.')
        self.player1.play_ships()
        print('Player 2\'s turn.')
        self.player2.play_ships()
        self.round += 1
        while not self.is_end():
            print('Round %d.' % self.round)
            print('Player 1\'s turn.')
            self.player1.attack(self.player2)
            if self.is_end():
                break
            print('Player 2\'s turn.')
            self.player2.attack(self.player1)
            self.round += 1

    def is_end(self):
        if self.player1.victory:
            print('Player 1 wins.')
            return True
        elif self.player2.victory:
            print('Player 2 wins.')
            return True
        else:
            return False

if __name__ == '__main__':
    new_game = Game()
    new_game.play()

