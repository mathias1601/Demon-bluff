from server.CardTypes.Card import Card
import random

class Knight(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Knight"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def execute(self):
        if self.isEvil() == False:
            return 0
        elif self.isCorrupted() == False:
            return -8
        else:
            return -1
    
    def getDescription(self):
        return "I can't die" 