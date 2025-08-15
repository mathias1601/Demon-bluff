class Card():

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):

        self.positionIndex = positionIndex
        self.deck = deck
        self.villager = isVillager
        self.outcast = isOutcast
        self.minion = isMinion
        self.demon = isDemon

        self.revealed = False

    def getType(self):
        if self.demon:
            return "evil"
        if self.minion:
            return "evil"
    
    def getPositionIndex(self):
        return self.positionIndex
    
    def reveal(self):
        return
        
    def execute(self):

        if self.getType() == "evil":
            return 0
        else:
            return -5
    

    """ Usage is meant to show if a card has a use-function. 
    If not it returns 0, it it does it returns the amount of indexes it should get """
    def getUsage(self):
        return 0
    
        
        

