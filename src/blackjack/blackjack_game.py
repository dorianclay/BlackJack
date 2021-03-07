import sys

from library.game import Game
from library.cli.prompt import Prompt
from src.blackjack.point_evaluator import evaluate_points

MAX_POINTS = 21

class BlackjackGame(Game):
  def __init__(self, dealer, players):
    super().__init__(dealer, players)
    self.current_player_index = 0

  def hit_player(self):
    player = self.current_player()
    self.dealer.draw(player)
    player_points = evaluate_points(player.cards)
    if player_points > MAX_POINTS:
      self.end_current_players_turn()

  def current_player(self):
    return self.players[self.current_player_index]

  def end_current_players_turn(self):
    self.current_player_index = self.current_player_index + 1

  def is_game_over(self):
    return self.current_player_index >= len(self.players)