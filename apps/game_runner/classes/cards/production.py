from .world import World

class Production(World):
    def __init__(self, cost, points, types, color):
        super().__init__(cost, points, types)
        self.color = color
        self.goods = False
        