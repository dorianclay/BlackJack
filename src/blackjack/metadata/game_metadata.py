from src.blackjack.metadata.player_metadata import PlayerMetadata

class GameMetadata:
  def __init__(self, player_metadata, other_players_metadata, is_game_over):
    self.player_metadata = player_metadata
    self.other_players_metadata = other_players_metadata
    self.is_game_over = is_game_over

  def json_repr(self):
    return {
      'is_game_over': self.is_game_over,
      'you': self.player_metadata.json_repr(),
      'players': [metadata.json_repr() for metadata in self.other_players_metadata]
    }

  def reveal_all_cards(self):
    for metadata in self.other_players_metadata:
      metadata.reveal_all_cards()

  @staticmethod
  def from_game(game, main_player):
    main_player_metadata = None
    other_players_metadata = []
    for player in game.players:
      metadata = PlayerMetadata.from_player(player)
      metadata.is_their_turn = player == game.current_player()
      if player == main_player:
        main_player_metadata = metadata
        main_player_metadata.reveal_all_cards()
        continue
      other_players_metadata.append(metadata)
    return GameMetadata(main_player_metadata, other_players_metadata, game.is_game_over())
