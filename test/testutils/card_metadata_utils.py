from src.blackjack.metadata.card_metadata import CardMetadata


def suits_from_card_json(cards_json):
    return sorted(
        [card_json[CardMetadata.Keys.suit] for card_json in cards_json])


def values_from_card_json(cards_json):
    return sorted(
        [card_json[CardMetadata.Keys.value] for card_json in cards_json])
