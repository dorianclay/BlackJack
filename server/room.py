from library.game_code import gen

class GameContext:

    def __init__(self, game):
        self.game = game
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

    def has_game_started(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return False
        return game_context.has_started

    def start_game(self, game_id):
        game_context = self.games.get(game_id)
        if not game_context:
            return
        game_context.has_started = True
