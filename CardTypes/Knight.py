from Card import Card
import random

class Knight(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Knight"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def execute(self):
        if self.villager:
            return 0
        else:
            return -8
        