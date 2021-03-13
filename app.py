import uuid

from flask import Flask, request
from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame
from src.blackjack.metadata.game_metadata import GameMetadata
from src.blackjack.validation import Validation

app = Flask(__name__)

main_deck = GameDeck([Deck()])
players = [Player('Computer')]
dealer = BlackjackDealer(main_deck)
game = BlackjackGame(dealer, players)
validation = Validation(game)


def get_player(player_id):
    for player in game.players:
        if player.id == player_id:
            return player


@app.route('/blackjack/api/v1/games/<game_id>/players/<player_id>')
def get_game(game_id, player_id):
    # TODO: Utilize game_id.
    player = get_player(uuid.UUID(player_id))
    if player is None:
        return '', 502
    meta = GameMetadata.from_game(game, player)
    return meta.json_repr()


@app.route('/blackjack/api/v1/players/<player_id>/hit')
def hit_player(player_id):
    player = players[0]
    if validation.player_can_hit(player.id):
        game.hit_player()
        return '', 204
    return '', 502


@app.route('/blackjack/api/v1/players/<player_id>/stay')
def stay_player(player_id):
    player = players[0]
    if validation.is_players_turn(player.id):
        game.end_current_players_turn()
        return '', 204
    return '', 502


@app.route('/blackjack/api/v1/players', methods=['POST'])
def create_player():
    name = request.json['name']
    new_player = Player(name)
    game.players.append(new_player)
    return str(new_player.id)


app.run()
