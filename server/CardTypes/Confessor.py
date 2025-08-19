from Card import Card
import random

class Confessor(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Confessor"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):

        self.revealed = True

        if self.villager:
            return "I am good"
        else:
            return "I am dizzy"