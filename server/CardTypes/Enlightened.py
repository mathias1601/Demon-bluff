from Card import Card
import random

class Englightened(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Enlightened"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def reveal(self):
        deck_size = len(self.deck)

        # Clockwise distance
        cw_distance = None
        for i in range(deck_size):
            idx = (self.positionIndex + i) % deck_size
            if self.deck[idx].getType() == "evil":
                cw_distance = i
                break

        # Counter-clockwise distance
        ccw_distance = None
        for i in range(deck_size):
            idx = (self.positionIndex - i) % deck_size
            if self.deck[idx].isEvil():
                ccw_distance = i
                break

        if cw_distance < ccw_distance:
            return "The closest evil is clockwise"
        elif ccw_distance < cw_distance:
            return "The closest evil is counterclockwise"
        else:
            return "The closest evil is equidistant"

