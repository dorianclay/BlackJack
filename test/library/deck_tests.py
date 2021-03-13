import unittest

from library.card import Card
from library.card import Suit
from library.deck import Deck


class DeckTestCase(unittest.TestCase):

    def test_number_of_cards(self):
        deck = Deck()
        self.assertEqual(52, len(deck.cards))

    def test_thirteen_cards_per_suit(self):
        suit_lists = {
            Suit.CLUBS: 0,
            Suit.HEARTS: 0,
            Suit.DIAMONDS: 0,
            Suit.SPADES: 0,
        }
        deck = Deck()
        for card in deck.cards:
            counter = suit_lists[card.suit]
            suit_lists[card.suit] = counter + 1
        for counter in suit_lists.values():
            self.assertEqual(13, counter)

    def test_unique_values_within_each_suit(self):
        cards_by_suit = {
            Suit.CLUBS: [],
            Suit.HEARTS: [],
            Suit.DIAMONDS: [],
            Suit.SPADES: [],
        }
        deck = Deck()
        for card in deck.cards:
            cards_by_suit[card.suit].append(card)
        for suit in Suit:
            cards_to_compare = cards_by_suit[suit]
            for value in range(1, 14):
                compare_card = Card(value, suit)
                self.assertIn(compare_card, cards_to_compare)


if __name__ == '__main__':
    unittest.main()
