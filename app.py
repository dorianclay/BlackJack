from flask import Flask
import json
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


@app.route('/blackjack')
def blackjack():
    return 'HelloWorld'


@app.route('/blackjack/api/v1/game')
def getGame():
    meta = GameMetadata.from_game(game, players[0])
    return json.dumps(meta.json_repr())


@app.route('/blackjack/api/v1/players/<id>/hit')
def hit_player(id):
    player = players[0]
    if validation.is_players_turn(player.id) and validation.player_can_hit(
            player.id):
        game.hit_player()
        return '', 204
    return '', 502


@app.route('/blackjack/api/v1/players/<id>/stay')
def stay_player(id):
    return ''


@app.route('/blackjack/api/v1/players')
def getPlayers():
    return ''


app.run()
