from .world import World

class Windfall(World):
    def __init__(self, cost, points, types, color):
        super().__init__(cost, points, types)
        self.cost = cost
        self.goods = True
