import uuid


class Player(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.cards = []

    def __eq__(self, other):
        return self.id == other.id
