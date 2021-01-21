from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='battleship',
    version='1.0.0',
    description='Demo of a Battleship board game in Python.',
    url='https://github.com/CoultonF/Xerris',
    author='Coulton Fraser',
    author_email='cjrfraser@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Click',
        'numpy',
        'pytest'
    ],
    entry_points='''
        [console_scripts]
        battleship=Xerris.battleship.app:cli
    '''
)