import sys

from library.game import Game
from library.cli.prompt import Prompt
from src.blackjack.point_evaluator import evaluate_points

MAX_POINTS = 21


class BlackjackGame(Game):

    def __init__(self, dealer, players):
        super().__init__(dealer, players)
        self.current_player_index = 0

    def hit_player(self):
        player = self.current_player()
        self.dealer.draw(player)
        player_points = evaluate_points(player.cards)
        if player_points > MAX_POINTS:
            self.end_current_players_turn()

    def current_player(self):
        if self.is_game_over():
            return None
        return self.players[self.current_player_index]

    def end_current_players_turn(self):
        self.current_player_index = self.current_player_index + 1

    def is_players_turn(self, player):
        if self.is_game_over():
            return False
        return player == self.current_player()

    def is_game_over(self):
        return self.current_player_index >= len(self.players)

    def get_winners(self):
        winning_score = self.get_winning_score()
        winning_players = []
        for player in self.players:
            score = evaluate_points(player.cards)
            if score == winning_score:
                winning_players.append(player)
        return winning_players

    def get_winning_score(self):
        scores = [evaluate_points(player.cards) for player in self.players]
        max_score = max(scores)
        while max_score > MAX_POINTS:
            scores.remove(max_score)
            if len(scores) == 0:
                return 0
            max_score = max(scores)
        return max_score
