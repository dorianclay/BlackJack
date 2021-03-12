from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame
from src.blackjack.cli.blackjack_cli import BlackjackCLI
from src.blackjack.cli.game_view import draw_game_view
from src.blackjack.metadata.game_metadata import GameMetadata

def main():
  print('Welcome to Dorian\'s Black Jack.')
  main_deck = GameDeck([Deck(), Deck()])
  players = [Player('Ben'), Player('Dorian')]
  dealer = BlackjackDealer(main_deck)
  game = BlackjackGame(dealer, players)
  cli = BlackjackCLI(game)

  dealer.deal(players)

  while not game.is_game_over():
    print_table(game)
    cli.prompt_user()

  print_table(game)


def print_table(game):
  metadata = get_game_metadata(game)
  draw_game_view(metadata.json_repr())


def get_game_metadata(game):
  current_player = get_current_player(game)
  return GameMetadata.from_game(game, current_player)


def get_current_player(game):
  if game.is_game_over():
    return game.players[-1]
  return game.current_player()


if __name__ == '__main__':
  main()