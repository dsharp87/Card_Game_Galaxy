from .card import Card

class Development(Card):
    def __init__(self, cost, points, types):
        super().__init__(cost, points, types)
        self.cost = cost
        self.points = points
        self.types = types