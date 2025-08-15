from Card import Card

class Judge(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Judge"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def use(self, position):

        if self.villager:

            if self.deck[position].getType() == "evil":
                return f"#{position} is lying"
            else:
                return f"#{position} is telling the truth"
        
        else:

            return f"#{position} is telling the truth"
        
    def getUsage(self):
        return 1
        
