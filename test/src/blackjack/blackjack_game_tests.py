import unittest

from library.card import Card
from library.card import Suit
from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame

class PointEvaluatorTestCase(unittest.TestCase):

  def setUp(self):
    deck = Deck()
    game_deck = GameDeck([deck])
    self.dealer = BlackjackDealer(game_deck)

  def test_hit_player(self):
    test_player = Player('test')
    game = BlackjackGame(self.dealer, [test_player])
    self.assertEqual(0, len(test_player.cards))
    game.hit_player()
    self.assertEqual(1, len(test_player.cards))

    game = create_game_with_cards([Card(1, Suit.SPADES)])
    player = game.current_player()
    game.hit_player()
    self.assertEqual(1, len(test_player.cards))
    self.assertEqual(Suit.SPADES, player.cards[0].suit)
    self.assertEqual(1, player.cards[0].value)

  def test_hit_player_and_bust_ends_turn(self):
    # Deck will only have 3 cards, each valued at 10.
    cards = [Card(10, Suit.SPADES)] * 3
    game = create_game_with_cards(cards)
    second_player_name = 'second player'
    second_player = Player(second_player_name)
    game.players.append(second_player)
    player = game.current_player()
    self.assertEqual(0, len(player.cards))
    game.hit_player()
    game.hit_player()
    # Score should be 20.
    # Still on player 1.
    self.assertEqual(game.players[0], player)
    # Now hit again to bust.
    game.hit_player()
    self.assertEqual(second_player, game.current_player())
    self.assertEqual(second_player_name, game.current_player().name)

  def test_hit_last_player_and_bust_ends_game(self):
    cards = [Card(10, Suit.SPADES)] * 3
    game = create_game_with_cards(cards)
    game.hit_player()
    game.hit_player()
    game.hit_player()
    self.assertTrue(game.is_game_over())

  def test_end_current_players_turn_moves_to_next_player(self):
    player1 = Player('1')
    player2 = Player('2')
    player3 = Player('3')
    game = BlackjackGame(self.dealer, [player1, player2, player3])
    self.assertEqual(player1, game.current_player())
    game.end_current_players_turn()
    self.assertEqual(player2, game.current_player())
    game.end_current_players_turn()
    self.assertEqual(player3, game.current_player())
    game.end_current_players_turn()
    self.assertTrue(game.is_game_over())

  def test_is_game_over_with_one_player(self):
    player1 = Player('1')
    game = BlackjackGame(self.dealer, [player1])
    game.end_current_players_turn()
    self.assertTrue(game.is_game_over())

  def test_get_max_winning_score(self):
    cards = [Card(10, Suit.SPADES)] * 2
    cards += [Card(5, Suit.SPADES)] * 2
    game = create_game_with_cards(cards)
    second_player_name = 'second player'
    second_player = Player(second_player_name)
    game.players.append(second_player)
    game.hit_player()
    game.hit_player()
    game.end_current_players_turn()
    game.hit_player()
    game.hit_player()
    self.assertEqual(20, game.get_winning_score())

  def test_get_max_winning_score_is_zero_for_tie(self):
    cards = [Card(10, Suit.SPADES)] * 6
    game = create_game_with_cards(cards)
    second_player_name = 'second player'
    second_player = Player(second_player_name)
    game.players.append(second_player)
    game.hit_player()
    game.hit_player()
    game.hit_player()
    # Now it's second player's turn because player 1 busted.
    game.hit_player()
    game.hit_player()
    game.hit_player()
    self.assertEqual(0, game.get_winning_score())

  def test_get_winning_players(self):
    # Cards are drawn in FILO order, so the result of the following insertion
    # will be the draw of [5, 5, 10, 10].
    cards = [Card(10, Suit.SPADES)] * 2
    cards += [Card(5, Suit.SPADES)] * 2
    game = create_game_with_cards(cards)
    second_player_name = 'second player'
    second_player = Player(second_player_name)
    game.players.append(second_player)
    game.hit_player()
    game.hit_player()
    game.end_current_players_turn()
    game.hit_player()
    game.hit_player()
    winners = game.get_winners()
    self.assertEqual(1, len(winners))
    self.assertEqual(second_player, winners[0])

def create_game_with_cards(cards):
  deck = Deck()
  deck.cards = cards
  game_deck = GameDeck([deck])
  dealer = BlackjackDealer(game_deck)
  test_player = Player('test')
  return BlackjackGame(dealer, [test_player])


if __name__ == '__main__':
    unittest.main()