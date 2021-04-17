import json
import unittest

from server.app import *
from src.blackjack.metadata.game_metadata import GameMetadata
from src.blackjack.metadata.player_metadata import PlayerMetadata
from uuid import UUID


class AppTestCase(unittest.TestCase):

    def test_creating_game(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            game = room.get_game(game_id)
            self.assertEqual(game_id, game.id)

    def test_start_game_prevents_new_players(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            c.post(f'blackjack/api/v1/games/{game_id}/start')
            # Now that the game has started, we should fail to create a player.
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            self.assertTrue(response.status.startswith('502'))

    def test_player_cannot_hit_before_game_starts(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            player_id = UUID(response.json['player_id'])
            # The game has NOT stared; player should fail to hit.
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{player_id}/hit')
            self.assertTrue(response.status.startswith('502'))

    def test_player_cannot_stay_before_game_starts(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            player_id = UUID(response.json['player_id'])
            # The game has NOT stared; player should fail to stay.
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{player_id}/stay')
            self.assertTrue(response.status.startswith('502'))

    def test_adding_player_to_game(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            player_id = UUID(response.json['player_id'])
            game = room.get_game(game_id)
            player = game.players[0]
            self.assertEquals(1, len(game.players))
            self.assertEquals('Ben Rooke', player.name)
            self.assertEquals(player_id, player.id)

    def test_player_hit(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            player_id = UUID(response.json['player_id'])
            c.post(f'blackjack/api/v1/games/{game_id}/start')
            game = room.get_game(game_id)
            player = game.players[0]
            self.assertEqual(0, len(player.cards))
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{player_id}/hit')
            self.assertEqual(1, len(player.cards))

    def test_player_hit_but_not_their_turn(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            first_player_id = UUID(response.json['player_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Dorian Clay'})
            second_player_id = UUID(response.json['player_id'])
            c.post(f'blackjack/api/v1/games/{game_id}/start')
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{second_player_id}/hit'
            )
            self.assertTrue(response.status.startswith('502'))

    def test_player_stay(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            c.post(f'/blackjack/api/v1/games/{game_id}/players',
                   json={'name': 'Dorian Clay'})
            c.post(f'blackjack/api/v1/games/{game_id}/start')
            player_id = UUID(response.json['player_id'])
            game = room.get_game(game_id)
            player = game.players[0]
            self.assertEqual(0, len(player.cards))
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{player_id}/stay')
            self.assertEqual(0, len(player.cards))
            self.assertNotEqual(player, game.current_player())

    def test_player_stay_but_not_their_turn(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            c.post(f'/blackjack/api/v1/games/{game_id}/players',
                   json={'name': 'Dorian Clay'})
            c.post(f'blackjack/api/v1/games/{game_id}/start')
            player_id = UUID(response.json['player_id'])
            game = room.get_game(game_id)
            player = game.players[0]
            self.assertEqual(0, len(player.cards))
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{player_id}/stay')
            self.assertEqual(0, len(player.cards))
            self.assertNotEqual(player, game.current_player())
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{player_id}/stay')
            self.assertTrue(response.status.startswith('502'))

    def test_get_game_state(self):
        with app.test_client() as c:
            response = c.post('/blackjack/api/v1/games')
            game_id = UUID(response.json['game_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Ben Rooke'})
            first_player_id = UUID(response.json['player_id'])
            response = c.post(f'/blackjack/api/v1/games/{game_id}/players',
                              json={'name': 'Dorian Clay'})
            second_player_id = UUID(response.json['player_id'])
            c.post(f'blackjack/api/v1/games/{game_id}/start')
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{first_player_id}')
            self.assertEqual(
                'Ben Rooke',
                response.json[GameMetadata.Keys.you][PlayerMetadata.Keys.name])
            self.assertEqual(
                'Dorian Clay', response.json[GameMetadata.Keys.players][0][
                    PlayerMetadata.Keys.name])
            response = c.get(
                f'/blackjack/api/v1/games/{game_id}/players/{second_player_id}')
            self.assertEqual(
                'Dorian Clay',
                response.json[GameMetadata.Keys.you][PlayerMetadata.Keys.name])
            self.assertEqual(
                'Ben Rooke', response.json[GameMetadata.Keys.players][0][
                    PlayerMetadata.Keys.name])


if __name__ == '__main__':
    unittest.main()
