from library.card import Card
from library.card import Suit

CARDS_PER_SUIT = 13


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in Suit:
            suited_cards = [
                Card(value, suit) for value in range(1, CARDS_PER_SUIT + 1)
            ]
            self.cards.extend(suited_cards)
