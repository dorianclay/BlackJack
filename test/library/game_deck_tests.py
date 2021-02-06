import random
import unittest

from library.card import Card
from library.card import Suit
from library.game_deck import GameDeck
from library.deck import Deck
from unittest.mock import MagicMock

class GameDeckTestCase(unittest.TestCase):
  def test_shuffles_all_cards(self):
    decks = [Deck(), Deck(), Deck()]
    all_cards = []
    for deck in decks:
      all_cards.extend(deck.cards)
    random.shuffle = MagicMock(return_value=all_cards)
    game_deck = GameDeck(decks)
    game_deck.shuffle()
    random.shuffle.assert_called_with(all_cards)

  def test_draws_card(self):
    expected_card = Card(1, Suit.HEARTS)
    deck = Deck()
    deck.cards = [expected_card]
    game_deck = GameDeck([deck])
    drawn_card = game_deck.draw()
    self.assertEqual(expected_card, drawn_card)


if __name__ == '__main__':
    unittest.main()