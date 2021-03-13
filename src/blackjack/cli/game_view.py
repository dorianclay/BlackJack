from src.blackjack.cli.player_view import draw_player_view


def draw_game_view(game_json):
    other_players_json = game_json['players']
    for other_player_json in other_players_json:
        draw_player_view(other_player_json)

    print('-' * 24)

    you_json = game_json['you']
    draw_player_view(you_json)

    print()

    if game_json.get('results') is not None:
        draw_results(game_json['results'])


def draw_results(results_json):
    if results_json['result'] == 'Tie':
        draw_message('No one won this round.')
        return
    winning_player_metadata = results_json['winning_player']
    winning_name = winning_player_metadata['name']
    winning_score = winning_player_metadata['score']
    draw_message('We have a winner!!!')
    draw_player_view(winning_player_metadata)
    print(f'{winning_name} won this round, with a score of {winning_score}')
    print()
    print('-' * 24)
    print()
    print()


def draw_message(message):
    print('-' * 24)
    print(message)
    print('-' * 24)
