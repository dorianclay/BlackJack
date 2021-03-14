import uuid


class Game(object):

    def __init__(self, dealer, players):
        self.id = uuid.uuid4()
        self.dealer = dealer
        self.players = players

    def take_turn(self):
        pass

    def __eq__(self, other):
        return self.id == other.id
