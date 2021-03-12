import unittest

from library.card import Card
from library.card import Suit
from src.blackjack.metadata.card_metadata import CardMetadata

class CardMetadataTestCase(unittest.TestCase):
  def test_card_suit_and_value(self):
    card = Card(5, Suit.SPADES)
    card_metadata = CardMetadata.from_card(card)
    card_json = card_metadata.json_repr()
    self.assertEqual('Spades', card_json[CardMetadata.Keys.suit])
    self.assertEqual('5', card_json[CardMetadata.Keys.value])
    self.assertFalse(card_json[CardMetadata.Keys.is_hidden])

  def test_card_suit_and_value(self):
    card = Card(5, Suit.SPADES)
    card_metadata = CardMetadata.from_card(card)
    card_metadata.is_hidden = True
    card_json = card_metadata.json_repr()
    self.assertIsNone(card_json.get(CardMetadata.Keys.suit))
    self.assertIsNone(card_json.get(CardMetadata.Keys.value))
    self.assertTrue(card_json[CardMetadata.Keys.is_hidden])


if __name__ == '__main__':
  unittest.main()