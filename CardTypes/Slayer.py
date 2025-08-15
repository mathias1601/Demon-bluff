from Card import Card
import random

class Slayer(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Slayer"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def use(self, position):
    

        if self.villager:

            if self.deck[position].getType() == "evil":
                self.deck[position].execute()
                return f"I slayed #{position}"

        else:

            return f"I cannot slay #{position}"
        
    def getUsage(self):
        return 1