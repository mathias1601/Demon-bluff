from Card import Card
import random

class Jester(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Jester"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def use(self, position1, position2, position3):

        allPositions = [position1, position2, position3]

        evilCount = 0

        for position in allPositions:
            if self.deck[position].isEvil():
                evilCount += 1

        if self.isEvil() == False and self.isCorrupted() == False:
            return f"Amongst #{position1}, #{position2} and #{position3}, there are {evilCount} evil(s)"
        else:

            maxEvils = 0
            for card in self.deck:
                if card.isEvil():
                    maxEvils += 1
            
            maxRandom = 0
            if maxEvils >= 3:
                maxRandom = 3
            else:
                maxRandom = maxEvils

            randomCount = random.randint(0, maxRandom)
            while randomCount == evilCount:
                randomCount = random.randint(0, maxRandom)

            return f"Amongst #{position1}, #{position2} and #{position3}, there are {randomCount} evil(s)"


        
    def getUsage(self):
        return 3