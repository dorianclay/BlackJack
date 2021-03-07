import uuid

class Player(object):
  def __init__(self, name):
    self.id = uuid.uuid4()
    self.name = name
    self.cards = []