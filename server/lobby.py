class Lobby():

    def __init__(self):
        self.players = []
        self.ready_player_ids = set()

    def get_ready_players(self, ignore_player_id):
        return [
            player for player in self.players if
            player.id != ignore_player_id and player.id in self.ready_player_ids
        ]

    def get_not_ready_players(self, ignore_player_id):
        return [
            player for player in self.players
            if player.id != ignore_player_id and
            player.id not in self.ready_player_ids
        ]

    def set_player_ready(self, player_id):
        self.ready_player_ids.add(player_id)

    def is_everyone_ready(self):
        for player in self.players:
            if player.id not in self.ready_player_ids:
                return False
        return True
