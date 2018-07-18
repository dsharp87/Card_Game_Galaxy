class Card(object):
    def __init__(self, cost, points, types):
        self.p1 = []
        self.p2 = []
        self.p3 = []
        self.p4t = []
        self.p4c = []
        self.p5 = []
        self.cost = cost
        self.points = points
        self.types = types

    def get_class_name(self):
        return self.__class__.__name__


