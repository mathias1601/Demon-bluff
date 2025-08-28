from Card import Card

class Minion(Card):
    """ The disguise parameter is meant to be a good villager class """
    def __init__(self, disguise):
        self.name = "Minion"
        self.disguise = disguise

    def getName(self):
        return self.disguise.name
    
    def getEvilName(self):
        return self.name
    
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
    
    def gameStart(self):
        return
    
    def isCorrupted(self):
        return False
    
    def getDescription(self):
        return self.disguise.getDescription()

    def getEvilDescription(self):
        return "I Lie and Disguise"

    def getHint(self):
        return self.disguise.getHint()
    
    def getEvilHint(self):
        return 
