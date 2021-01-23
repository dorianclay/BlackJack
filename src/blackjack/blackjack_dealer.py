from library.dealer import Dealer

class BlackjackDealer(Dealer):

  INITIAL_CARD_COUNT = 2

  def deal(self, players):
    for i in range(BlackjackDealer.INITIAL_CARD_COUNT):
      for player in players:
        player.cards.append(self.game_deck.draw())
  
  def draw(self, player):
    player.cards.append(self.game_deck.draw())