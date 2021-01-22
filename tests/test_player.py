from battleship.player import Player
import pytest


class TestPlayer:

    @pytest.mark.parametrize("opponent,pos,coord,modifier,victory", [
        (Player(), (0, 0), 'A1', Player().ships[0].id, True),
        (Player(), (1, 1), 'A1', Player().ships[0].id, False)
    ])
    def test_attack(self, mocker, opponent, pos, coord, modifier, victory):
        player = Player()
        new_pos = tuple(2 * m for m in pos)
        opponent.board.area[new_pos] = opponent.ships[0].id()
        mocker.patch('builtins.input', side_effect=[coord])
        player.attack(opponent)
        assert player.victory == victory

    @pytest.mark.parametrize("rotate,coords", [
        (['n'], ['A1']),
        (['n'], ['A7', 'A1'])
    ])
    def test_play_ships(self, mocker, rotate, coords):
        player = Player()
        mocker.patch('builtins.input', side_effect=rotate + coords)
        player.play_ships()
        num, alpha = player.coordinates.split(coords[-1])
        num = player.coordinates.numeric_index(num)
        alpha = player.coordinates.alpha_index(alpha)
        assert player.board.area[(num, alpha)] == player.ships[0].id()
