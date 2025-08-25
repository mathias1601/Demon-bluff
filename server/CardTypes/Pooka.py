from Minion import Minion

class Pooka(Minion):
    """ The disguise parameter is meant to be a good villager class """
    def __init__(self, disguise):
        self.name = "Pooka"
        self.disguise = disguise

    def gameStart(self):
        self.disguise.deck[self.getPositionIndex() + 1].corrupted = True
        self.disguise.deck[self.getPositionIndex() - 1].corrupted = True