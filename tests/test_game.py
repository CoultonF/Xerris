from battleship.game import Game
import pytest
import numpy as np


class TestGame:

    @pytest.mark.parametrize("win,expected", [
        (True, True),
        (False, False)
    ])
    def test_is_end(self, win, expected):
        game = Game()
        game.player1.victory = win
        game.player2.defeat = win
        assert game.is_end() == expected

    @pytest.mark.parametrize("ship_placements,invalid_loc,expected", [
        (["y", "1a", "n", "1a"], ['0a'], True),
        (["n", "1a", "y", "1a"], [], False)
    ])
    def test_play(self, mocker, ship_placements, invalid_loc, expected):
        game = Game()
        actions = self.make_all_actions(game.player1.board.rows, game.player1.board.cols)
        mocker.patch('builtins.input', side_effect=ship_placements + invalid_loc + actions)
        game.play()
        assert game.player2.victory == expected

    def make_all_actions(self, m, n):
        # m & n are board row & cols
        # a 1d array that simulates all moves for 2 players.
        player_moves = np.indices((m, n)).transpose(1, 2, 0).flatten()
        moves = []
        for i in range(1, len(player_moves), 2):
            moves.append(str(player_moves[i - 1]+1) + self.num_to_alpha(player_moves[i]))
        actions = np.empty((len(player_moves)), dtype='<U2')
        actions[0::2] = moves
        actions[1::2] = moves
        return actions.tolist()

    def num_to_alpha(self, n):
        header = ''
        n += 1
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            header = chr(65 + remainder) + header
        return header
