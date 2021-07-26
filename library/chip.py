from enum import Enum

class Color(Enum):
    WHITE = 1
    YELLOW = 2
    RED = 3
    BLUE = 4
    GREY = 5
    GREEN = 6
    ORANGE = 7
    BLACK = 8
    PINK = 9
    PURPLE = 10
    BURGUNDY = 11
    LIGHTBLUE = 12
    BROWN = 13

class Chip(object):

    def __init__(self, color):
        self.color = color
        self.value = self.colorToVal()

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color
    
    def colorToVal(self):
        colors = {
            Color.WHITE: 1,
            Color.YELLOW: 2,
            Color.RED: 5,
            Color.BLUE: 10,
            Color.GREY: 20,
            Color.GREEN: 25,
            Color.ORANGE: 50,
            Color.BLACK: 100,
            Color.PINK: 250,
            Color.PURPLE: 500,
            Color.BURGUNDY: 1000,
            Color.LIGHTBLUE: 2000,
            Color.BROWN: 5000
        }
        return colors[self.color]

    def colorToString(self):
        colors = {
            Color.WHITE: 'White',
            Color.YELLOW: 'Yellow',
            Color.RED: 'Red',
            Color.BLUE: 'Blue',
            Color.GREY: 'Grey',
            Color.GREEN: 'Green',
            Color.ORANGE: 'Orange',
            Color.BLACK: 'Black',
            Color.PINK: 'Pink',
            Color.PURPLE: 'Purple',
            Color.BURGUNDY: 'Burgundy',
            Color.LIGHTBLUE: 'Light Blue',
            Color.BROWN: 'Brown'
        }
        return colors[self.color]


    def __eq__(self, other_card):
        return self.value == other_card.value

    def __repr__(self):
        return self.colorToString() + ' \t(' + str(self.value) + ')'