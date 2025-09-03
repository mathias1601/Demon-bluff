from server.CardTypes.Card import Card
import random

class Confessor(Card):

    def __init__(self, positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon):
        self.name = "Confessor"
        super().__init__(positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):

        if self.isEvil() or self.corrupted:
            return "I am dizzy"
        else:
            return "I am good"
        
    def getDescription(self):
        return "If I am Evil or Corrupted: \"I am dizzy\"  "
    
    def getHint(self):
        return "I can not Lie"
    
    