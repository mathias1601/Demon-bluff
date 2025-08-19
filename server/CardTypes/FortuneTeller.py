from Card import Card
import random

class FortuneTeller(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Fortune Teller"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def use(self, position1, position2):
        
        if self.villager:
            if self.deck[position1].isEvil() or self.deck[position2].isEvil():
                return f"Is #{position1} or #{position2} evil?: True"
            else:
                return f"Is #{position1} or #{position2} evil?: False"
        else:
            if self.deck[position1].isEvil() or self.deck[position2].isEvil():
                return f"Is #{position1} or #{position2} evil?: False"
            else:
                return f"Is #{position1} or #{position2} evil?: True"
            
    def getUsage(self):
        return 2