POINTS_WITH_ROOM_FOR_ACE = 11


def evaluate_points(cards):
    points = 0
    for card in cards:
        points = points + get_card_points(card)
    for card in cards:
        if card.value == 1 and points <= POINTS_WITH_ROOM_FOR_ACE:
            points = points + 10
    return points


def get_card_points(card):
    if card.value > 10:
        return 10
    return card.value
