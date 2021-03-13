def draw_cards_json(cards_json):
    all_card_lines = [get_card_lines(card_json) for card_json in cards_json]
    for i in range(6):
        i_line_for_each_card = [card_lines[i] for card_lines in all_card_lines]
        print(' '.join(i_line_for_each_card))


def get_card_lines(card_json):
    if card_json['is_hidden']:
        return get_hidden_card_lines()
    short_title = get_short_card_title(card_json['value'])
    short_suit = get_short_card_suit(card_json['suit'])
    return get_visible_card_lines(short_title, short_suit)


def get_visible_card_lines(short_title, short_suit):
    edge = ('*' * 7)
    empty_space = '*' + (' ' * 5) + '*'
    return [
        edge,
        empty_space,
        add_line_suffix(f'*  {short_title}'),
        add_line_suffix(f'*  {short_suit}'),
        empty_space,
        edge,
    ]


def get_hidden_card_lines():
    edge = ('*' * 7) + ' '
    return [edge for _ in range(6)]


def add_line_suffix(line):
    '''Adds the final space and card edge.'''
    if len(line) == 5:
        return line + ' *'
    return line + '  *'


def get_short_card_title(card_title):
    if card_title == 'Ace':
        return 'A'
    if card_title == 'Jack':
        return 'J'
    if card_title == 'Queen':
        return 'Q'
    if card_title == 'King':
        return 'K'
    return card_title


def get_short_card_suit(card_suit):
    return card_suit[0]
