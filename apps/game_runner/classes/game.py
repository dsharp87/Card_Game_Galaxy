from .player import Player
from .deck import Deck

class Game(object):
    def __init__(self, players, expansions):
        self.players = []
        self.status = "playing"
        self.deck = Deck(expansions)
        self.discard = []
        for i in range(0, len(players)):
            self.players.append(Player(players[i][0], players[i][1], self.deck))
        
    def round(self):
        # per player, pick round card
        # load player/round choice into array so phases know how to provide bonuses
        # per phase:
            # per player:
                # check if they get bonus and apply modifiser as nessiccsary 
                # promt if action will be taken or start action and prompt response
                # end player action
            # end phase
        # per player
            # evaluate discards requirement
            # evaluate if player has reached end game
        return self

    def explore(self):
        # params = player, deck, modifier(s) - both from card choises as well as player buffs array[]
        # based on modifyer:
            # draw 2, discard 1
            # draw 3, discard 1
            # draw 7, discard 6
        # end phase
        return self

    def develop(self):
        # params = player, modifers - both from card and buffs
        # call player_card
        # end phase
        return self

    def settle(self):
        # params = player, modifers - both from card and buffs
        # call player_card
        # end phase
        return self

    def trade(self):
        # params
        return self


    def WinChecker(self):
        #create point total storage array
        # per player:
            # total up points
        # probably return full score array and the wining player?
        return self
