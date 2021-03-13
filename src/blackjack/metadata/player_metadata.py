from src.blackjack.point_evaluator import evaluate_points
from src.blackjack.metadata.card_metadata import CardMetadata


class PlayerMetadata:

    class Keys:
        name = 'name'
        score = 'score'
        their_turn = 'their_turn'
        cards = 'cards'

    def __init__(self, name, score, card_metadata):
        self.name = name
        # Score is hidden by default.
        self.show_score = False
        self.score = score
        self.card_metadata = card_metadata
        self.is_their_turn = False

    def json_repr(self):
        json = {
            PlayerMetadata.Keys.name:
                self.name,
            PlayerMetadata.Keys.their_turn:
                self.is_their_turn,
            PlayerMetadata.Keys.cards: [
                metadata.json_repr() for metadata in self.card_metadata
            ]
        }
        if self.show_score:
            json[PlayerMetadata.Keys.score] = self.score
        return json

    def reveal_all_cards(self):
        # Reveal the score as well.
        self.show_score = True
        for metadata in self.card_metadata:
            metadata.is_hidden = False

    @staticmethod
    def from_player(player):
        score = evaluate_points(player.cards)
        card_metadata = [CardMetadata.from_card(card) for card in player.cards]
        # Hide a player's first card.
        if len(card_metadata) > 0:
            card_metadata[0].is_hidden = True
        return PlayerMetadata(player.name, score, card_metadata)
