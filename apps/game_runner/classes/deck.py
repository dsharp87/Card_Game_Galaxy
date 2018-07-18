from .cards.development import Development
from .cards.production import Production
from .cards.windfall import Windfall
from .cards.world import World
import random

class Deck(object):
    def __init__(self, expansions):
        self.cards = []
        self.create_deck(expansions)

    def create_deck(self, expansions):
        for i in range(0,5):
            self.cards.append(Production(5, 3, ["uplift"], "green"))
            self.cards.append(Production(4, 3, ["military", "rebel"], "brown"))
            self.cards.append(Windfall(3, 2, ["alien"], "yellow"))
            self.cards.append(Windfall(2, 1, ["military", "rebel"], "blue"))
            self.cards.append(World(5, 4, []))
            self.cards.append(World(3, 2, []))
            self.cards.append(World(2, 1, []))
            self.cards.append(Development(6, 4, []))
            self.cards.append(Development(5, 4, []))
            self.cards.append(Development(4, 3, []))
            self.cards.append(Development(3, 2, ["uplift"]))
            self.cards.append(Development(2, 1, ["rebel"]))
            self.cards.append(Development(1, 0, []))
        self.shuffle()
        return self

    def shuffle(self):
        for i in range(0, len(self.cards)):
            idx = random.randint(0,len(self.cards))
            temp = self.cards[idx]
            self.cards[idx] = self.cards[i]
            self.cards[i] = temp
        return self

