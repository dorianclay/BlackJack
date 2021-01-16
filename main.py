from deck import Deck

def main():
  print('Welcome to Dorian\'s Black Jack.')
  main_deck = Deck()
  for card in main_deck.cards:
    print(card)

if __name__ == '__main__':
  main()