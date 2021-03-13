from src.blackjack.cli.card_view import draw_cards_json


def draw_player_view(player_json):
    is_current_player = player_json['their_turn']
    draw_name(player_json, is_current_player)
    draw_score(player_json, is_current_player)
    draw_cards_json(player_json['cards'])


def draw_name(player_json, is_current_player):
    name_prefix = ''
    if is_current_player:
        name_prefix = 'You: '
    name = player_json['name']
    print(f'{name_prefix}{name}')


def draw_score(player_json, is_current_player):
    if is_current_player:
        score = player_json['score']
        print(f'Score: {score}')
