import unittest

from library.card import Card
from library.card import Suit
from library.deck import Deck
from library.player import Player
from src.blackjack.metadata.card_metadata import CardMetadata
from src.blackjack.metadata.player_metadata import PlayerMetadata
from test.testutils.card_metadata_utils import *

class PlayerMetadataTestCase(unittest.TestCase):
  def test_cards_and_score_are_shown(self):
    player_name = 'test'
    player = Player(player_name)
    player.cards = [
      Card(1, Suit.DIAMONDS),
      Card(11, Suit.SPADES),
    ]
    player_metadata = PlayerMetadata.from_player(player)
    player_metadata.reveal_all_cards()
    player_json = player_metadata.json_repr()
    cards_json = player_json[PlayerMetadata.Keys.cards]
    self.assertEqual(player_name, player_json[PlayerMetadata.Keys.name])
    self.assertEqual(21, player_json[PlayerMetadata.Keys.score])
    for (index, card_json) in enumerate(cards_json):
      self.assertEqual(player.cards[index].suitToString(), card_json[CardMetadata.Keys.suit])
      self.assertEqual(player.cards[index].valToFace(), card_json[CardMetadata.Keys.value])

  def test_cards_and_score_hidden(self):
    player_name = 'test'
    player = Player(player_name)
    player.cards = [
      Card(13, Suit.DIAMONDS),
      Card(10, Suit.SPADES),
    ]
    player_metadata = PlayerMetadata.from_player(player)
    player_json = player_metadata.json_repr()
    cards_json = player_json[PlayerMetadata.Keys.cards]
    self.assertEqual(player_name, player_json[PlayerMetadata.Keys.name])
    self.assertIsNone(player_json.get(PlayerMetadata.Keys.score))
    self.assertEqual(2, len(player_json[PlayerMetadata.Keys.cards]))
    # Hidden card.
    self.assertIsNone(cards_json[0].get(CardMetadata.Keys.suit))
    self.assertIsNone(cards_json[0].get(CardMetadata.Keys.value))
    # Revealed card.
    revealed_card_json = cards_json[1]
    self.assertEqual(player.cards[1].suitToString(), revealed_card_json[CardMetadata.Keys.suit])
    self.assertEqual(player.cards[1].valToFace(), revealed_card_json[CardMetadata.Keys.value])

  def test_score_hidden(self):
    player_name = 'test'
    player = Player(player_name)
    player.cards = [
      Card(13, Suit.DIAMONDS),
      Card(10, Suit.SPADES),
    ]
    player_metadata = PlayerMetadata.from_player(player)
    player_json = player_metadata.json_repr()
    self.assertIsNone(player_json.get(PlayerMetadata.Keys.score))


if __name__ == '__main__':
  unittest.main()