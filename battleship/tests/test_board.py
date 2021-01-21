from battleship.ship import Ship
from battleship.board import Board
import pytest


class TestBoard:
    @pytest.mark.parametrize("ship,pos,expected", [
        (Ship(), (0, 0), True),
        (Ship(), (6, 6), False),
        (Ship(1, 1), (8, 8), False),
        (Ship(1, 3), (7, 7), False),
        (Ship(1, 3), (6, 6), False)
    ])
    def test_place_ship(self, ship, pos, expected):
        board = Board()
        result = board.place_ship(ship, pos)
        assert result == expected


    @pytest.mark.parametrize("ship_id,modifier,expected", [
        (Ship().id(), Board._Board__EMPTY, True),
        (Ship().id(), Ship().id(), False)
    ])
    def test_has_remaining_ships(self, ship_id, modifier, expected):
        board = Board()
        board.area[0][0] = modifier
        assert board.has_remaining_ships(ship_id) == expected


    @pytest.mark.parametrize("ship,pos,expected", [
        (Ship(), (0, 0), True),
        (Ship(), (6, 6), False),
        (Ship(1, 1), (8, 8), False),
        (Ship(1, 3), (7, 7), False),
        (Ship(1, 3), (6, 6), False)
    ])
    def test_update(self):
        assert False
