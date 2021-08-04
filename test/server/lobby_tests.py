import unittest

from library.player import Player
from server.lobby import Lobby


class LobbyTestCase(unittest.TestCase):

    def test_player_exists_true(self):
        lobby = Lobby()
        expected_player = Player('Bob')
        lobby.players.append(expected_player)
        lobby.players.append(Player('Alice'))
        lobby.players.append(Player('Thor'))
        self.assertTrue(lobby.player_exists(expected_player.id))

    def test_player_exists_false(self):
        lobby = Lobby()
        unexpected_player = Player('Bob')
        lobby.player.append(Player('Alice'))
        lobby.player.append(Player('Thor'))
        self.assertFalse(lobby.player_exists(unexpected_player.id))
    
    def test_get_ready_players(self):
        lobby = Lobby()
        expected_ready_player = Player('ready')
        lobby.players.append(expected_ready_player)
        lobby.players.append(Player('not_ready_player'))
        lobby.ready_player_ids.add(expected_ready_player.id)
        self.assertEqual(lobby.get_ready_players(''), [expected_ready_player])

    def test_get_ready_players_ignoring_passed_id(self):
        lobby = Lobby()
        expected_ready_player = Player('ready')
        ignored_player = Player('ignored_player')
        lobby.players.append(expected_ready_player)
        lobby.players.append(ignored_player)
        lobby.ready_player_ids.add(expected_ready_player.id)
        lobby.ready_player_ids.add(ignored_player.id)
        self.assertEqual(lobby.get_ready_players(ignored_player.id),
                         [expected_ready_player])

    def test_get_not_ready_players(self):
        lobby = Lobby()
        expected_ready_player = Player('ready')
        not_ready_player = Player('not_ready_player')
        lobby.players.append(expected_ready_player)
        lobby.players.append(not_ready_player)
        lobby.ready_player_ids.add(expected_ready_player.id)
        self.assertEqual(lobby.get_not_ready_players(''), [not_ready_player])

    def test_is_everyone_ready_true(self):
        lobby = Lobby()
        player1 = Player('player1')
        player2 = Player('player2')
        lobby.players.append(player1)
        lobby.players.append(player2)
        lobby.ready_player_ids.add(player1.id)
        lobby.ready_player_ids.add(player2.id)
        self.assertTrue(lobby.is_everyone_ready())

    def test_is_everyone_ready_false(self):
        lobby = Lobby()
        player1 = Player('player1')
        lobby.players.append(player1)
        lobby.players.append(Player('player2'))
        lobby.ready_player_ids.add(player1.id)
        self.assertFalse(lobby.is_everyone_ready())


if __name__ == '__main__':
    unittest.main()
