from src.blackjack.metadata.player_metadata import PlayerMetadata
from src.blackjack.metadata.results_metadata import ResultsMetadata


class GameMetadata:

    class Keys:
        you = 'you'
        players = 'players'
        results = 'results'
        has_started = 'has_started'

    def __init__(self, player_metadata, other_players_metadata,
                 results_metadata, has_started):
        self.player_metadata = player_metadata
        self.other_players_metadata = other_players_metadata
        self.results_metadata = results_metadata
        self.has_started = has_started

    def json_repr(self):
        json = {
            GameMetadata.Keys.you: self.player_metadata.json_repr(),
            GameMetadata.Keys.players: [
                metadata.json_repr() for metadata in self.other_players_metadata
            ],
            GameMetadata.Keys.has_started: self.has_started
        }
        if self.results_metadata is not None:
            json[GameMetadata.Keys.results] = self.results_metadata.json_repr()
        return json

    def reveal_all_cards(self):
        for metadata in self.other_players_metadata:
            metadata.reveal_all_cards()

    @staticmethod
    def from_game(game, main_player, has_started):
        other_players = GameMetadata.get_other_players(game.players,
                                                       main_player)
        other_players_metadata = [
            GameMetadata.create_player_metadata(game, player)
            for player in other_players
        ]
        if game.is_game_over():
            for player_metadata in other_players_metadata:
                player_metadata.reveal_all_cards()
        main_player_metadata = GameMetadata.create_player_metadata(
            game, main_player)
        main_player_metadata.reveal_all_cards()
        return GameMetadata(main_player_metadata, other_players_metadata,
                            ResultsMetadata.from_game(game), has_started)

    @staticmethod
    def get_other_players(players, main_player):
        return [player for player in players if player != main_player]

    @staticmethod
    def create_player_metadata(game, player, is_main_player=False):
        metadata = PlayerMetadata.from_player(player)
        if game.is_players_turn(player):
            metadata.is_their_turn = True
        if is_main_player:
            metadata.reveal_all_cards()
        return metadata
