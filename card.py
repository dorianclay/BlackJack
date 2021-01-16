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

  def __repr__(self):
    return f'{self.value} of {self.suit}'