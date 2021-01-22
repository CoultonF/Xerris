# Xerris
Coding interview question - battleship

### Requirements

- Python3.9 - https://www.python.org/downloads/release/python-390/
- Setuptools - https://pypi.org/project/setuptools/
- Tox - https://tox.readthedocs.io/en/latest/install.html

### Running

Run the test scripts.
```
python -m tox
or
python3 -m tox
```

Run the game.
```
python -m tox -e game
or
python3 -m tox -e game
```

### Directory Organization
```
.
├── battleship                  # Contains the source code for game classes
|   ├── board.py
|   ├── coordinates.py
|   ├── game.py
|   ├── player.py
|   └── ship.py
|
├── tests                       # Contains tests automated through setuptools
|   ├── __init__.py
|   ├── test_board.py
|   ├── test_coordinates.py
|   ├── test_game.py
|   ├── test_player.py
|   └── test_ship.py
|
├── setup.py                    # Setuptools configuration
└── tox.ini                     # Tox automated deployment and virtual environments
```
