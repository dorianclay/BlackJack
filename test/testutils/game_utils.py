from library.deck import Deck
from library.game_deck import GameDeck
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame


def create_game(cards, players):
  deck = Deck()
  deck.cards = cards
  game_deck = GameDeck([deck])
  dealer = BlackjackDealer(game_deck)
  return BlackjackGame(dealer, players)