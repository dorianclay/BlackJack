from src.blackjack.metadata.player_metadata import PlayerMetadata


class ResultsMetadata:

    class Keys:
        result = 'result'
        winning_player = 'winning_player'

    def __init__(self, winning_players_metadata):
        self.winning_players_metadata = winning_players_metadata

    def json_repr(self):
        if len(self.winning_players_metadata) != 1:
            return self.json_repr_for_tie()
        return self.json_repr_for_win()

    def json_repr_for_win(self):
        return {
            ResultsMetadata.Keys.result:
                'Win',
            ResultsMetadata.Keys.winning_player:
                self.winning_players_metadata[0].json_repr()
        }

    def json_repr_for_tie(self):
        return {ResultsMetadata.Keys.result: 'Tie'}

    @staticmethod
    def from_game(game):
        if not game.is_game_over():
            return None
        winning_players = game.get_winners()
        winning_players_metadata = [
            PlayerMetadata.from_player(player) for player in winning_players
        ]
        for metadata in winning_players_metadata:
            metadata.reveal_all_cards()
        return ResultsMetadata(winning_players_metadata)
