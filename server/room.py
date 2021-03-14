class Room:

    def __init__(self):
        self.games = {}

    def add_game(self, game):
        self.games[game.id] = game

    def get_game(self, game_id):
        return self.games.get(game_id)
