from src.blackjack.point_evaluator import evaluate_points
from src.blackjack.metadata.card_metadata import CardMetadata

class PlayerMetadata:
  def __init__(self, name, card_metadata):
    self.name = name
    # Score is hidden by default.
    self.score = None
    self.card_metadata = card_metadata
    self.is_their_turn = False

  def json_repr(self):
    return {
      'name': self.name,
      'score': self.score,
      'their_turn': self.is_their_turn,
      'cards': [metadata.json_repr() for metadata in self.card_metadata]
    }

  def reveal_all_cards(self):
    # Reveal the score as well.
    self.score = evaluate_points(player.cards)
    for metadata in self.card_metadata:
      metadata.is_hidden = False

  @staticmethod
  def from_player(player):
    card_metadata = [CardMetadata(card) for card in player.cards]
    # Hide a player's first card.
    card_metadata[0].is_hidden = True
    return PlayerMetadata(player.name, score, card_metadata)
