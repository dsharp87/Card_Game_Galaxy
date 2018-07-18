from .deck import Deck

class Player(object):
    def __init__(self, name, player_type, deck):
        self.name = name
        self.player_type = player_type
        self.hand = []
        self.board = []
        self.buffs = []
        self.draw(deck, 6)

    def draw(self, deck, amount):
        for i in range(0,amount):
            self.hand.append(deck.cards.pop())
        return self

# untested, unsure if will be able to pass game, not sure if this function will do or just call the funtion that modifies the player's buffs
    def play_card(self, hand_idx, payment_idx_arr, game):
        # also need modifers
        self.board.append(self.hand.pop(hand_idx))
        for idx in payment_idx_arr:
            game.discard.append(self.hand.pop(idx))
        # based on if type is development or world apply call draw funtion
        return self
        
        
