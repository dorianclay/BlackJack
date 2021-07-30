from library.game_code import gen
from library.player import Player
from server.lobby import Lobby


class GameContext:

    def __init__(self, game):
        self.game = game
        self.lobby = Lobby()
        self.has_started = False


class Room:

    def __init__(self):
        self.games = {}

    def add_game(self, game):
        new_game_id = gen()
        while new_game_id in self.games:
            new_game_id = gen()
        self.games[new_game_id] = GameContext(game)
        return new_game_id

    def get_game(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return None
        return game_context.game

    def get_lobby(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return None
        return game_context.lobby

    def add_player_to_lobby(self, game_id, player_name):
        game_context = self.games.get(game_id)
        if not game_context:
            return None
        new_player = Player(player_name)
        game_context.lobby.players.append(new_player)
        return new_player.id

    def has_game_started(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return False
        return game_context.has_started

    def get_lobby_list(self, game_id, player_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return None
        ready_players = game_context.lobby.get_ready_players(player_id)
        ready_player_strings = [
            f'{player.name} (ready)' for player in ready_players
        ]
        not_ready_players = game_context.lobby.get_not_ready_players(player_id)
        not_ready_player_strings = [player.name for player in not_ready_players]
        return ready_player_strings + not_ready_player_strings

    def set_player_ready(self, game_id, player_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return
        game_context.lobby.set_player_ready(player_id)

    def is_everyone_ready(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return False
        return game_context.lobby.is_everyone_ready()

    def is_player_ready(self, game_id, player_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return False
        return player_id in game_context.lobby.ready_player_ids

    def start_game(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return
        if not game_context.lobby.is_everyone_ready():
            return
        game_context.game.players = game_context.lobby.get_ready_players('')
        game_context.has_started = True
