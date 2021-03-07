from src.blackjack.blackjack_game import MAX_POINTS
from src.blackjack.point_evaluator import evaluate_points

class Validation():
  def __init__(self, game):
    self.game = game

  def is_player_turn(self, player_id):
    player = self.get_player(player_id)
    if player is None:
      return False
    return player == self.game.current_player()

  def player_can_hit(self, player_id):
    return (self.is_player_turn(player_id) and
        self.get_player_points(player_id) < MAX_POINTS)

  def get_player(self, player_id):
    for player in self.game.players:
      if player.id == player_id:
        return player

  def get_player_points(self, player_id):
    player = self.get_player(player_id)
    if player is None:
      return 0
    return evaluate_points(player.cards)
