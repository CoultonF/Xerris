import pytest
from battleship.coordinates import Coordinates


class TestCoordinates:
    @pytest.mark.parametrize("number,expected", [
        ('A', 0),
        ('Z', 25),
        ('AA', 26)
    ])
    def test_alpha_index(self, number, expected):
        coordinates = Coordinates()
        assert coordinates.alpha_index(number) == expected

    @pytest.mark.parametrize("number,expected", [
        ('1', 0),
        ('2', 1)
    ])
    def test_numeric_index(self, number, expected):
        coordinates = Coordinates()
        assert coordinates.numeric_index(number) == expected

    @pytest.mark.parametrize("coord,expected", [
        ('A1', ['1', 'A']),
        ('AA2', ['2', 'AA']),
        ('-5a', ['5', 'A']),
        ('5HJ54', ['5', 'HJ'])
    ])
    def test_split(self, coord, expected):
        coordinates = Coordinates()
        assert coordinates.split(coord) == expected

    @pytest.mark.parametrize("coord,expected", [
        ('A1', (0, 0)),
        ('d4', (3, 3))
    ])
    def test_get_pos(self, mocker, coord, expected):
        coordinates = Coordinates()
        mocker.patch('builtins.input', side_effect=[coord])
        assert coordinates.get_pos() == expected

