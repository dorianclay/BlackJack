import sys

from library.game import Game
from library.cli.prompt import Prompt
from src.blackjack.point_evaluator import evaluate_points

MAX_POINTS = 21

class BlackjackGame(Game):
  def __init__(self, dealer, players):
    super().__init__(dealer, players)
    self.current_player_index = 0
    self.action_map = {
      'Hit': self.hit_player,
      'Stay': self.next_player,
    }

  def take_turn(self):
    if not self.player_turns_left():
      return
    player = self.players[self.current_player_index]
    # Use dependency injection so BlackjackGame doesn't know about CLI Prompt.
    prompt = Prompt(f'{player.name}\'s turn.', self.action_map)
    prompt.act()

  def hit_player(self):
    player = self.players[self.current_player_index]
    self.dealer.draw(player)
    player_points = evaluate_points(player.cards)
    if player_points > MAX_POINTS:
      print('You bust!')
      self.next_player()
  
  def next_player(self):
    self.current_player_index = self.current_player_index + 1

  def player_turns_left(self):
    return self.current_player_index < len(self.players)