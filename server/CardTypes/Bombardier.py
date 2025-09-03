from server.CardTypes.Card import Card

class Bombardier(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Bombardier"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def execute(self):
        if self.isEvil() == False:
            return -10
        else:
            return -1 
        
    def getDescription(self):
        return "Lose if you Execute me"