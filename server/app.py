from uuid import UUID

from flask import Flask, request
from flask_cors import CORS
from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from server.room import Room
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame
from src.blackjack.metadata.game_metadata import GameMetadata
from src.blackjack.validation import Validation
from uuid import UUID

app = Flask(__name__)
CORS(app)

room = Room()


def get_player(player_id, game):
    for player in game.players:
        if player.id == player_id:
            return player


@app.route('/blackjack/api/v1/games', methods=['POST'])
def create_game():
    main_deck = GameDeck([Deck()])
    dealer = BlackjackDealer(main_deck)
    game = BlackjackGame(dealer, [])
    game_id = room.add_game(game)
    return {'game_id': game_id}


@app.route('/blackjack/api/v1/games/<game_id>', methods=['POST'])
def join_game(game_id):
    game = room.get_game(game_id)
    if game is None:
        return '', 502
    return '', 204


@app.route('/blackjack/api/v1/games/<game_id>/start', methods=['POST'])
def start_game(game_id):
    room.start_game(game_id)
    game = room.get_game(game_id)
    game.dealer.deal(game.players)
    return '', 204


@app.route('/blackjack/api/v1/games/<game_id>/players/<player_id>')
def get_game(game_id, player_id):
    game = room.get_game(game_id)
    has_started = room.has_game_started(game_id)
    player = get_player(UUID(player_id), game)
    if player is None:
        return '', 502
    meta = GameMetadata.from_game(game, player, has_started)
    return meta.json_repr()


@app.route('/blackjack/api/v1/games/<game_id>/players/<player_id>/hit')
def hit_player(game_id, player_id):
    if not room.has_game_started(game_id):
        return '', 502
    game = room.get_game(game_id)
    validation = Validation(game)
    if validation.player_can_hit(UUID(player_id)):
        game.hit_player()
        return '', 204
    return '', 502


@app.route('/blackjack/api/v1/games/<game_id>/players/<player_id>/stay')
def stay_player(game_id, player_id):
    if not room.has_game_started(game_id):
        return '', 502
    game = room.get_game(game_id)
    validation = Validation(game)
    if validation.is_players_turn(UUID(player_id)):
        game.end_current_players_turn()
        return '', 204
    return '', 502


@app.route('/blackjack/api/v1/games/<game_id>/players', methods=['POST'])
def create_player(game_id):
    if room.has_game_started(game_id):
        return '', 502
    game = room.get_game(game_id)
    name = request.json['name']
    new_player = Player(name)
    game.players.append(new_player)
    return {'player_id': new_player.id}


def run():
    app.run()
