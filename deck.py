from card import Card
from card import Suit

class Deck(object):
  def __init__(self):
    self.cards = []
    for suit in Suit:
      for card_value in range(1, 14):
        new_card = Card(card_value, suit)
        self.cards.append(new_card)
        