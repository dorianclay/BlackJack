import unittest

from library.card import Card
from library.card import Suit

class CardTestCase(unittest.TestCase):

  def test_create_card(self):
    test_value = 5
    test_suit = Suit.HEARTS
    card = Card(test_value, test_suit)
    self.assertEqual(test_value, card.value)
    self.assertEqual(test_suit, card.suit)

  def test_card_name_for_numeric_cards(self):
    for value in range(2, 11):
      card = Card(value, Suit.DIAMONDS)
      self.assertEqual(str(value), card.valToFace())

  def test_card_name_for_face_cards(self):
    card = Card(11, Suit.HEARTS)
    self.assertEqual('Jack', card.valToFace())
    card = Card(12, Suit.HEARTS)
    self.assertEqual('Queen', card.valToFace())
    card = Card(13, Suit.HEARTS)
    self.assertEqual('King', card.valToFace())
    card = Card(1, Suit.HEARTS)
    self.assertEqual('Ace', card.valToFace())

  def test_all_suits(self):
    for test_suit in Suit:
      card = Card(1, test_suit)
      self.assertEqual(test_suit, card.suit)

  def test_suit_to_string(self):
    test_pairs = [
      (Suit.CLUBS, 'Clubs'),
      (Suit.DIAMONDS, 'Diamonds'),
      (Suit.HEARTS, 'Hearts'),
      (Suit.SPADES, 'Spades'),
    ]
    for test_pair in test_pairs:
      suit = test_pair[0]
      expected_suit_string = test_pair[1]
      card = Card(1, suit)
      self.assertEqual(expected_suit_string, card.suitToString())


if __name__ == '__main__':
    unittest.main()