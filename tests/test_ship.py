from battleship.ship import Ship


class TestShip:

    def test_rotate(self):
        ship = Ship(1, 2)
        ship.rotate()
        assert ship.area.shape == (2, 1)

