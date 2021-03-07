from library.cli.choice import Choice
from library.cli.menu import Menu
from library.cli.prompt import Prompt

class BlackjackCLI:
  def __init__(self, game):
    self.game = game
    self.menu = Menu([
      Choice('Hit', self.hit),
      Choice('Stay', self.stay),
    ])

  def prompt_user(self):
    current_player = self.game.current_player()
    prompt_message = f'[{current_player.name}] Do you want to hit or stay?'
    prompt = Prompt(prompt_message, self.menu)
    choice_index = prompt.get_choice_index_from_menu()
    self.menu.make_choice(choice_index)

  def hit(self):
    self.game.hit_player()

  def stay(self):
    self.game.end_current_players_turn()
