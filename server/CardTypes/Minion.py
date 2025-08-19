class Minion():
    """ The disguise parameter is meant to be a good villager class """
    def __init__(self, disguise):
        self.name = "Minion"
        self.disguise = disguise

    def getName(self):
        return self.disguise.name
    
    def isEvil(self):
        return self.disguise.isEvil()
    
    def getPositionIndex(self):
        return self.disguise.getPositionIndex()
    
    def reveal(self):
        return self.disguise.reveal()
        
    def execute(self):
        return self.disguise.execute()
    
    def assignDeck(self, deck):
        self.disguise.deck = deck

    """ Usage is meant to show if a card has a use-function. 
    If not it returns 0, it it does it returns the amount of indexes it should get """
    def getUsage(self):
        return self.disguise.getUsage()