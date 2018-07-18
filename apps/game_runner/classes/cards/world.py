from .card import Card

class  World(Card):
    def __init__(self, cost, points, types):
        super().__init__(cost, points, types)
        self.cost = cost
        self.points = points
        self.types = types
        self.color = "colorless"
        self.military = False
