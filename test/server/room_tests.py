import unittest

from library.deck import Deck
from library.game_deck import GameDeck
from library.player import Player
from server.room import Room
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame


class RoomTestCase(unittest.TestCase):

    def test_get_room(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        self.assertTrue(game, room.get_game(str(game_id)))

    def test_get_room_with_multiple_rooms(self):
        deck1 = GameDeck([Deck()])
        deck2 = GameDeck([Deck(), Deck(), Deck()])
        dealer1 = BlackjackDealer(deck1)
        dealer2 = BlackjackDealer(deck2)
        game1 = BlackjackGame(dealer1, [])
        game2 = BlackjackGame(dealer2, [])
        room = Room()
        game1_id = room.add_game(game1)
        game2_id = room.add_game(game2)
        self.assertTrue(game1, room.get_game(str(game1_id)))
        self.assertTrue(game2, room.get_game(str(game2_id)))

    def test_get_room_but_no_rooms(self):
        id_str = 'code-code-code'
        room = Room()
        self.assertIsNone(room.get_game(id_str))

    def test_get_room_invalid_id(self):
        id_str = 'code-code-code'
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        room.add_game(game)
        self.assertIsNone(room.get_game(id_str))

    def test_has_started_returns_true(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        room.start_game(game_id)
        self.assertTrue(room.has_game_started(game_id))

    def test_has_started_returns_false(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        self.assertFalse(room.has_game_started(game_id))

    def test_isolation_of_start_game(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game1 = BlackjackGame(dealer, [])
        game2 = BlackjackGame(dealer, [])
        game3 = BlackjackGame(dealer, [])
        room = Room()
        game1_id = room.add_game(game1)
        game2_id = room.add_game(game2)
        game3_id = room.add_game(game3)
        room.start_game(game1_id)
        self.assertTrue(room.has_game_started(game1_id))
        self.assertFalse(room.has_game_started(game2_id))
        self.assertFalse(room.has_game_started(game3_id))

    def test_has_started_returns_false_if_not_ready(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        alice_player_id = room.add_player_to_lobby(game_id, 'alice')
        room.add_player_to_lobby(game_id, 'bob')
        room.set_player_ready(game_id, alice_player_id)
        room.start_game(game_id)
        self.assertFalse(room.has_game_started(game_id))

    def test_has_started_returns_true_if_everyone_is_ready(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        alice_player_id = room.add_player_to_lobby(game_id, 'alice')
        bob_player_id = room.add_player_to_lobby(game_id, 'bob')
        room.set_player_ready(game_id, alice_player_id)
        room.set_player_ready(game_id, bob_player_id)
        room.start_game(game_id)
        self.assertTrue(room.has_game_started(game_id))

    def test_get_ready_player_names(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        alice_player_id = room.add_player_to_lobby(game_id, 'alice')
        bob_player_id = room.add_player_to_lobby(game_id, 'bob')
        room.set_player_ready(game_id, alice_player_id)
        room.set_player_ready(game_id, bob_player_id)
        names = room.get_lobby_list(game_id, '')
        self.assertSetEqual(set(['alice (ready)', 'bob (ready)']), set(names))

    def test_get_ready_players_except_for_me(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        alice_player_id = room.add_player_to_lobby(game_id, 'alice')
        bob_player_id = room.add_player_to_lobby(game_id, 'bob')
        room.set_player_ready(game_id, alice_player_id)
        room.set_player_ready(game_id, bob_player_id)
        names = room.get_lobby_list(game_id, alice_player_id)
        self.assertSetEqual(set(['bob (ready)']), set(names))

    def test_get_not_ready_players(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        room.add_player_to_lobby(game_id, 'alice')
        room.add_player_to_lobby(game_id, 'bob')
        names = room.get_lobby_list(game_id, '')
        self.assertSetEqual(set(['alice', 'bob']), set(names))

    def test_get_ready_and_not_ready_players(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        room.add_player_to_lobby(game_id, 'alice')
        bob_player_id = room.add_player_to_lobby(game_id, 'bob')
        room.set_player_ready(game_id, bob_player_id)
        names = room.get_lobby_list(game_id, '')
        self.assertSetEqual(set(['bob (ready)', 'alice']), set(names))

    def test_does_return_player_as_ready(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        room.add_player_to_lobby(game_id, 'alice')
        bob_player_id = room.add_player_to_lobby(game_id, 'bob')
        room.set_player_ready(game_id, bob_player_id)
        self.assertTrue(room.is_player_ready(game_id, bob_player_id))

    def test_does_return_player_as_not_ready(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        game_id = room.add_game(game)
        room.add_player_to_lobby(game_id, 'alice')
        bob_player_id = room.add_player_to_lobby(game_id, 'bob')
        self.assertFalse(room.is_player_ready(game_id, bob_player_id))


if __name__ == '__main__':
    unittest.main()
