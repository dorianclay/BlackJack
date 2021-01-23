from game import Game

class BlackjackGame(Game):
  def __init__(self, dealer, players):
    super().__init__(dealer, players)
    self.current_player_index = 0

  def take_turn(self):
    self.dealer.draw(self.players[self.current_player_index])
    self.current_player_index = (self.current_player_index + 1) % len(self.players)