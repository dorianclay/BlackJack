class CardMetadata:

    class Keys:
        value = 'value'
        suit = 'suit'
        is_hidden = 'is_hidden'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.is_hidden = False

    def json_repr(self):
        if self.is_hidden:
            return self.json_repr_hidden()
        return {
            CardMetadata.Keys.value: self.value,
            CardMetadata.Keys.suit: self.suit,
            CardMetadata.Keys.is_hidden: False,
        }

    def json_repr_hidden(self):
        return {
            CardMetadata.Keys.is_hidden: True,
        }

    @staticmethod
    def from_card(card):
        return CardMetadata(card.valToFace(), card.suitToString())
