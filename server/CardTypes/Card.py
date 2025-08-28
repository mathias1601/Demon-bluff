class Card():

    def __init__(self, positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon):

        self.positionIndex = positionIndex
        self.deck = deck
        self.villager = isVillager
        self.corrupted = isCorrupted
        self.minion = isMinion
        self.demon = isDemon

        self.revealed = False

    def isEvil(self):
        if self.demon or self.minion:
            return True
        
        return False
    
    def isCorrupted(self):
        return self.corrupted
    
    def getPositionIndex(self):
        return self.positionIndex
    
    def reveal(self):
        return
        
    def execute(self):

        if self.isEvil():
            return -1
        else:
            return -5
    
    def assignDeck(self, deck):
        self.deck = deck

    """ Usage is meant to show if a card has a use-function. 
    If not it returns 0, it it does it returns the amount of indexes it should get """
    def getUsage(self):
        return 0
    
    def gameStart(self):
        return 
    
    def getDescription(self):
        return 
    
    def getHint(self):
        return 
    
    def getEvilName(self):
        return 
    
        
        

