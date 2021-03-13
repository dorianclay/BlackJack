from enum import Enum


class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def valToFace(self):
        faces = {
            1: 'Ace',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        return faces[self.value]

    def suitToString(self):
        suits = {
            Suit.CLUBS: 'Clubs',
            Suit.DIAMONDS: 'Diamonds',
            Suit.HEARTS: 'Hearts',
            Suit.SPADES: 'Spades'
        }
        return suits[self.suit]

    def __eq__(self, other_card):
        return self.value == other_card.value and self.suit == other_card.suit

    def __repr__(self):
        return self.valToFace() + ' \t' + self.suitToString()
