import unittest

from library.card import Card
from library.card import Suit
from library.player import Player
from src.blackjack.metadata.card_metadata import CardMetadata
from src.blackjack.metadata.game_metadata import GameMetadata
from src.blackjack.metadata.player_metadata import PlayerMetadata
from src.blackjack.metadata.results_metadata import ResultsMetadata
from src.blackjack.point_evaluator import evaluate_points
from test.testutils.card_metadata_utils import *
from test.testutils.game_utils import *


class GameMetadataTestCase(unittest.TestCase):

    def test_setting_turn(self):
        player_name = 'me'
        main_player = Player(player_name)
        other_players = [Player(name) for name in ['1', '2', '3']]
        game = create_game([], [main_player] + other_players)
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        you_json = game_json[GameMetadata.Keys.you]
        others_json = game_json[GameMetadata.Keys.players]
        # Player 1's turn.
        self.assertTrue(you_json[PlayerMetadata.Keys.their_turn])
        self.assertFalse(others_json[0][PlayerMetadata.Keys.their_turn])
        self.assertFalse(others_json[1][PlayerMetadata.Keys.their_turn])
        # Player 2's turn.
        game.end_current_players_turn()
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        you_json = game_json[GameMetadata.Keys.you]
        others_json = game_json[GameMetadata.Keys.players]
        self.assertFalse(you_json[PlayerMetadata.Keys.their_turn])
        self.assertTrue(others_json[0][PlayerMetadata.Keys.their_turn])
        self.assertFalse(others_json[1][PlayerMetadata.Keys.their_turn])
        # Player 3's turn.
        game.end_current_players_turn()
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        you_json = game_json[GameMetadata.Keys.you]
        others_json = game_json[GameMetadata.Keys.players]
        self.assertFalse(you_json[PlayerMetadata.Keys.their_turn])
        self.assertFalse(others_json[0][PlayerMetadata.Keys.their_turn])
        self.assertTrue(others_json[1][PlayerMetadata.Keys.their_turn])
        # No one's turn.
        game.end_current_players_turn()
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        you_json = game_json[GameMetadata.Keys.you]
        others_json = game_json[GameMetadata.Keys.players]
        self.assertFalse(you_json[PlayerMetadata.Keys.their_turn])
        self.assertFalse(others_json[0][PlayerMetadata.Keys.their_turn])
        self.assertFalse(others_json[1][PlayerMetadata.Keys.their_turn])

    def test_game_metadata_with_one_player(self):
        player_name = 'me'
        cards = [Card(10, Suit.SPADES), Card(2, Suit.HEARTS)]
        main_player = Player(player_name)
        game = create_game(cards, [main_player])
        game.hit_player()
        game.hit_player()
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        you_json = game_json[GameMetadata.Keys.you]
        cards_json = you_json[PlayerMetadata.Keys.cards]
        self.assertEqual(player_name, you_json[PlayerMetadata.Keys.name])
        self.assertEqual(12, you_json[PlayerMetadata.Keys.score])
        self.assertListEqual(['Hearts', 'Spades'],
                             suits_from_card_json(cards_json))
        self.assertListEqual(['10', '2'], values_from_card_json(cards_json))
        self.assertIsNone(game_json.get(GameMetadata.Keys.results))

    def test_game_metadata_with_multiple_players(self):
        player_name = 'me'
        main_player = Player(player_name)
        other_player_names = ['bob', 'alice']
        other_players = [Player(name) for name in other_player_names]
        all_cards = flat_cards_from_stack([
            [Card(1, Suit.SPADES)] * 3,
            [Card(2, Suit.HEARTS)] * 3,
            [Card(3, Suit.DIAMONDS)] * 3,
        ])
        game = create_game(all_cards, [main_player] + other_players)
        # Give everyone 3 cards.
        deal_to_player(game, 3)
        deal_to_player(game, 3)
        deal_to_player(game, 3)
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        others_json = game_json[GameMetadata.Keys.players]
        you_json = game_json[GameMetadata.Keys.you]
        cards_json = you_json[PlayerMetadata.Keys.cards]
        self.assertEqual(player_name, you_json[PlayerMetadata.Keys.name])
        self.assertEqual(13, you_json[PlayerMetadata.Keys.score])
        self.assertListEqual(['Spades'] * 3, suits_from_card_json(cards_json))
        self.assertListEqual(['Ace'] * 3, values_from_card_json(cards_json))
        # Test other players.
        for player_index in range(0, 2):
            expected_player = game.players[player_index + 1]
            # We remove the first value of each of these lists, since the first card
            # will be hidden from the main player.
            expected_suits = players_expected_suits(expected_player)
            expected_values = players_expected_values(expected_player)
            cards_json = others_json[player_index][PlayerMetadata.Keys.cards]
            first_card_json, remaining_cards_json = hidden_and_shown(cards_json)
            self.assertEqual(expected_player.name,
                             other_player_names[player_index])
            self.assertIsNone(others_json[player_index].get(
                PlayerMetadata.Keys.score))
            # First card of other player should be hidden.
            self.assertTrue(first_card_json[CardMetadata.Keys.is_hidden])
            self.assertEqual(expected_suits,
                             suits_from_card_json(remaining_cards_json))
            self.assertListEqual(expected_values,
                                 values_from_card_json(remaining_cards_json))

    def test_game_metadata_with_one_player_and_game_is_over(self):
        player_name = 'me'
        cards = [
            Card(10, Suit.SPADES),
            Card(10, Suit.HEARTS),
            Card(1, Suit.DIAMONDS)
        ]
        main_player = Player(player_name)
        game = create_game(cards, [main_player])
        game.hit_player()
        game.hit_player()
        game.hit_player()
        game.end_current_players_turn()
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        results_json = game_json[GameMetadata.Keys.results]
        you_json = game_json[GameMetadata.Keys.you]
        cards_json = you_json[PlayerMetadata.Keys.cards]
        self.assertEqual(player_name, you_json[PlayerMetadata.Keys.name])
        self.assertEqual(21, you_json[PlayerMetadata.Keys.score])
        self.assertListEqual(['Diamonds', 'Hearts', 'Spades'],
                             suits_from_card_json(cards_json))
        self.assertListEqual(['10', '10', 'Ace'],
                             values_from_card_json(cards_json))
        self.assertEqual('Win', results_json[ResultsMetadata.Keys.result])

    def test_game_metadata_with_multiple_players_and_game_is_over(self):
        main_player = Player('me')
        other_player_names = ['bob', 'alice']
        other_players = [Player(name) for name in other_player_names]
        all_cards = flat_cards_from_stack([
            [Card(2, Suit.SPADES)] * 3,
            [Card(2, Suit.HEARTS)] * 3,
            [Card(3, Suit.DIAMONDS)] * 3,
        ])
        game = create_game(all_cards, [main_player] + other_players)
        # Give everyone 3 cards.
        deal_to_player(game, 3)
        deal_to_player(game, 3)
        deal_to_player(game, 3)
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        results_json = game_json[GameMetadata.Keys.results]
        winning_player_json = results_json[ResultsMetadata.Keys.winning_player]
        others_json = game_json[GameMetadata.Keys.players]
        expected_winner = game.players[2]
        expected_suits = players_expected_suits(expected_winner)
        expected_values = players_expected_values(expected_winner)
        cards_json = others_json[1][PlayerMetadata.Keys.cards]
        first_card_json, remaining_cards_json = hidden_and_shown(cards_json)
        self.assertEqual(expected_winner.name, other_player_names[1])
        self.assertIsNone(others_json[1].get(PlayerMetadata.Keys.score))
        # First card of other player should be hidden.
        self.assertTrue(first_card_json[CardMetadata.Keys.is_hidden])
        self.assertEqual(expected_suits,
                         suits_from_card_json(remaining_cards_json))
        self.assertListEqual(expected_values,
                             values_from_card_json(remaining_cards_json))
        self.assertEqual('Win', results_json[ResultsMetadata.Keys.result])
        self.assert_winner_is_player(expected_winner, winning_player_json)

    def test_game_metadata_with_multiple_players_and_game_is_over_tie(self):
        player_name = 'Me'
        main_player = Player(player_name)
        other_player_names = ['bob', 'alice']
        other_players = [Player(name) for name in other_player_names]
        all_cards = flat_cards_from_stack([
            [Card(2, Suit.SPADES)] * 4,
            [Card(4, Suit.HEARTS)] * 2,
            [Card(8, Suit.DIAMONDS)] * 1,
        ])
        game = create_game(all_cards, [main_player] + other_players)
        deal_to_player(game, 4)
        deal_to_player(game, 2)
        deal_to_player(game, 1)
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        results_json = game_json[GameMetadata.Keys.results]
        self.assertEqual('Tie', results_json[ResultsMetadata.Keys.result])

    def test_game_metadata_with_multiple_players_and_game_is_over_everyone_busts(
            self):
        player_name = 'Me'
        main_player = Player(player_name)
        other_player_names = ['bob', 'alice']
        other_players = [Player(name) for name in other_player_names]
        all_cards = flat_cards_from_stack([
            [Card(10, Suit.SPADES)] * 3,
            [Card(9, Suit.HEARTS)] * 3,
            [Card(4, Suit.DIAMONDS)] * 6,
        ])
        game = create_game(all_cards, [main_player] + other_players)
        deal_to_player(game, 3)
        deal_to_player(game, 3)
        deal_to_player(game, 6)
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        results_json = game_json[GameMetadata.Keys.results]
        self.assertEqual('Tie', results_json[ResultsMetadata.Keys.result])
    
    def test_game_started(self):
        main_player = Player('Me')
        game = create_game([], [main_player])
        game_metadata = GameMetadata.from_game(game, main_player, True)
        game_json = game_metadata.json_repr()
        self.assertTrue(game_json[GameMetadata.Keys.has_started])
    
    def test_game_not_started(self):
        main_player = Player('Me')
        game = create_game([], [main_player])
        game_metadata = GameMetadata.from_game(game, main_player, False)
        game_json = game_metadata.json_repr()
        self.assertFalse(game_json[GameMetadata.Keys.has_started])

    def assert_winner_is_player(self, player, player_json):
        points = evaluate_points(player.cards)
        cards_json = player_json[PlayerMetadata.Keys.cards]
        expected_suits = [card.suitToString() for card in player.cards]
        expected_values = [card.valToFace() for card in player.cards]
        self.assertEqual(player.name, player_json[PlayerMetadata.Keys.name])
        self.assertEqual(points, player_json[PlayerMetadata.Keys.score])
        self.assertEqual(expected_suits, suits_from_card_json(cards_json))
        self.assertListEqual(expected_values, values_from_card_json(cards_json))


def flat_cards_from_stack(card_stack):
    # Cards are dealt in FILO (reverse of how it was defined). Reversing so our
    # declaration is read in the same order players get cards.
    card_stack.reverse()
    return [card for cards in card_stack for card in cards]


def deal_to_player(game, num_of_cards):
    current_player = game.current_player()
    for _ in range(num_of_cards):
        game.hit_player()
    # Only end the current players turn if it is still their turn.
    if game.is_players_turn(current_player):
        game.end_current_players_turn()


def hidden_and_shown(cards_json):
    '''Returns the single hidden card and the remaining shown cards.'''
    return (cards_json[0], cards_json[1:])


def players_expected_suits(player):
    '''Returns all suits except the first card because it should be hidden.'''
    return [card.suitToString() for card in player.cards][1:]


def players_expected_values(player):
    '''Returns all values except the first card because it should be hidden.'''
    return [card.valToFace() for card in player.cards][1:]


def suits_from_card_json(cards_json):
    return sorted(
        [card_json[CardMetadata.Keys.suit] for card_json in cards_json])


def values_from_card_json(cards_json):
    return sorted(
        [card_json[CardMetadata.Keys.value] for card_json in cards_json])


if __name__ == '__main__':
    unittest.main()
