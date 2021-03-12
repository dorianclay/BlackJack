import unittest

from library.card import Card
from library.card import Suit
from library.player import Player
from src.blackjack.metadata.player_metadata import PlayerMetadata
from src.blackjack.metadata.results_metadata import ResultsMetadata
from test.testutils.game_utils import *

class ResultsMetadataTestCase(unittest.TestCase):
  def test_no_results_yet(self):
    players = [Player(name) for name in ['1', '2', '3']]
    game = create_game([], players)
    # Game is not over yet, no results to generate.
    results_metadata = ResultsMetadata.from_game(game)
    self.assertIsNone(results_metadata)

  def test_with_no_winners(self):
    players = [Player(name) for name in ['1', '2', '3']]
    game = create_game([], players)
    while not game.is_game_over():
      game.end_current_players_turn()
    results_metadata = ResultsMetadata.from_game(game)
    results_json = results_metadata.json_repr()
    self.assertIsNone(results_json.get(ResultsMetadata.Keys.winning_player))
    self.assertEqual('Tie', results_json[ResultsMetadata.Keys.result])

  def test_with_winner(self):
    cards = [
      Card(1, Suit.HEARTS)
    ]
    players = [Player(name) for name in ['1', '2', '3']]
    game = create_game(cards, players)
    winning_player_index = 1
    for _ in range(winning_player_index):
      game.end_current_players_turn()
    game.hit_player()
    while not game.is_game_over():
      game.end_current_players_turn()
    results_metadata = ResultsMetadata.from_game(game)
    results_json = results_metadata.json_repr()
    winner_json = results_json[ResultsMetadata.Keys.winning_player]
    winner_name = winner_json[PlayerMetadata.Keys.name]
    self.assertEqual(players[winning_player_index].name, winner_json[PlayerMetadata.Keys.name])
    self.assertEqual(11, winner_json[PlayerMetadata.Keys.score])
    self.assertEqual('Win', results_json[ResultsMetadata.Keys.result])

  def test_with_multiple_winners_is_tie(self):
    cards = [Card(10, Suit.DIAMONDS)] * 4
    players = [Player(name) for name in ['1', '2', '3']]
    game = create_game(cards, players)
    # Skip first player, so there is one loser.
    game.end_current_players_turn()
    # Next two players hit twice.
    for _ in range(2):
      game.hit_player()
      game.hit_player()
      game.end_current_players_turn()
    results_metadata = ResultsMetadata.from_game(game)
    results_json = results_metadata.json_repr()
    self.assertIsNone(results_json.get(ResultsMetadata.Keys.winning_player))
    self.assertEqual('Tie', results_json[ResultsMetadata.Keys.result])

  def test_winner_because_everyone_else_busts(self):
    cards = [Card(10, Suit.DIAMONDS)] * 6
    players = [Player(name) for name in ['1', '2', '3']]
    game = create_game(cards, players)
    # Skip first player, so everyone else busts.
    game.end_current_players_turn()
    while not game.is_game_over():
      game.hit_player()
    results_metadata = ResultsMetadata.from_game(game)
    results_json = results_metadata.json_repr()
    winner_json = results_json[ResultsMetadata.Keys.winning_player]
    self.assertEqual('1', winner_json[PlayerMetadata.Keys.name])
    self.assertEqual(0, winner_json[PlayerMetadata.Keys.score])


if __name__ == '__main__':
  unittest.main()