class CardMetadata:
  def __init__(self, card):
    self.card = card
    self.is_hidden = False

  def json_repr(self):
    if self.is_hidden:
      return self.json_repr_hidden()
    return {
      'value': self.card.valToFace(),
      'suit': self.card.suitToString(),
      'is_hidden': False,
    }

  def json_repr_hidden(self):
    return {
      'is_hidden': True,
    }
