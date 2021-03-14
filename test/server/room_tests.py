import unittest

from library.deck import Deck
from library.game_deck import GameDeck
from server.room import Room
from src.blackjack.blackjack_dealer import BlackjackDealer
from src.blackjack.blackjack_game import BlackjackGame
from uuid import UUID


class RoomTestCase(unittest.TestCase):

    def test_get_room(self):
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        room.add_game(game)
        self.assertTrue(game, room.get_game(str(game.id)))

    def test_get_room_with_multiple_rooms(self):
        deck1 = GameDeck([Deck()])
        deck2 = GameDeck([Deck(), Deck(), Deck()])
        dealer1 = BlackjackDealer(deck1)
        dealer2 = BlackjackDealer(deck2)
        game1 = BlackjackGame(dealer1, [])
        game2 = BlackjackGame(dealer2, [])
        room = Room()
        room.add_game(game1)
        room.add_game(game2)
        self.assertTrue(game1, room.get_game(str(game1.id)))
        self.assertTrue(game2, room.get_game(str(game2.id)))

    def test_get_room_but_no_rooms(self):
        id_str = '12345678123456781234567812345678'
        uuid = UUID(id_str)
        room = Room()
        self.assertIsNone(room.get_game(id_str))

    def test_get_room_invalid_id(self):
        id_str = '12345678123456781234567812345678'
        uuid = UUID(id_str)
        deck = GameDeck([Deck()])
        dealer = BlackjackDealer(deck)
        game = BlackjackGame(dealer, [])
        room = Room()
        room.add_game(game)
        self.assertIsNone(room.get_game(id_str))


if __name__ == '__main__':
    unittest.main()
