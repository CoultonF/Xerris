from setuptools import setup, find_packages

setup(
    name='battleship',
    version='1.0.0',
    description='Demo of a Battleship board game in Python.',
    url='https://github.com/CoultonF/Xerris',
    author='Coulton Fraser',
    author_email='cjrfraser@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pytest',
        'pytest-mock'
    ],
)