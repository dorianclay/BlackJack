from deck import Deck
from game_deck import GameDeck

def main():
  print('Welcome to Dorian\'s Black Jack.')
  main_deck = GameDeck([Deck(), Deck()])
  for iter in range(10):
    print(main_deck.draw())

if __name__ == '__main__':
  main()