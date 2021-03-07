import unittest

from library.card import Card
from library.card import Suit
from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame
from src.blackjack.validation import Validation
from uuid import UUID

class ValidationTestCase(unittest.TestCase):
  def setUp(self):
    self.test_player = Player('test')
    deck = Deck()
    game_deck = GameDeck([deck])
    dealer = BlackjackDealer(game_deck)
    game = BlackjackGame(dealer, [self.test_player])
    self.validation = Validation(game)

  def test_is_players_turn(self):
    is_players_turn = self.validation.is_player_turn(self.test_player.id)
    self.assertTrue(is_players_turn)

  def test_is_not_players_turn(self):
    wrong_uuid = UUID('12345678123456781234567812345678')
    is_players_turn = self.validation.is_player_turn(wrong_uuid)
    self.assertFalse(is_players_turn)

  def test_player_can_hit_under_21(self):
    cards = [
      Card(5, Suit.HEARTS),
      Card(6, Suit.DIAMONDS),
    ]
    self.test_player.cards = cards
    can_hit = self.validation.player_can_hit(self.test_player.id)
    self.assertTrue(can_hit)

  def test_player_cannot_hit_at_21(self):
    cards = [
      Card(5, Suit.HEARTS),
      Card(6, Suit.DIAMONDS),
      Card(10, Suit.SPADES),
    ]
    self.test_player.cards = cards
    can_hit = self.validation.player_can_hit(self.test_player.id)
    self.assertFalse(can_hit)

  def test_player_cannot_hit_over_21(self):
    cards = [
      Card(5, Suit.HEARTS),
      Card(6, Suit.DIAMONDS),
      Card(10, Suit.SPADES),
      Card(13, Suit.CLUBS),
    ]
    self.test_player.cards = cards
    can_hit = self.validation.player_can_hit(self.test_player.id)
    self.assertFalse(can_hit)


if __name__ == '__main__':
  unittest.main()