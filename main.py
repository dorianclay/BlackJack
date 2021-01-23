from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame

from time import sleep

def main():
  print('Welcome to Dorian\'s Black Jack.')
  main_deck = GameDeck([Deck(), Deck()])
  players = [Player('Ben'), Player('Dorian')]
  dealer = BlackjackDealer(main_deck)
  game = BlackjackGame(dealer, players)

  dealer.deal(players)
  print_players(players)

  sleep(2)
  game.take_turn()
  print_players(players)
  sleep(2)
  game.take_turn()
  print_players(players)
  sleep(2)
  game.take_turn()
  print_players(players)

def print_players(players):
  for player in players:
    print(f'{player.name}\'s hand')
    for card in player.cards:
      print("\t", card)
  

if __name__ == '__main__':
  main()