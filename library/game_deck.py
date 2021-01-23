import random

class GameDeck(object):
  def __init__(self, decks):
    """
    Initializes the gamedeck to the decks passed in.
      :param decks: an array of decks.
    """
    self.decks = decks
    self.shuffle()

  def shuffle(self):
    self.cards = []
    for deck in self.decks:
      self.cards.extend(deck.cards)
    random.shuffle(self.cards)
  
  def draw(self):
    return self.cards.pop()