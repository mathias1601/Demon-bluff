from Card import Card
import random

class Oracle(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Oracle"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):
        
        currentEvils = []
        for i in range(len(self.deck)):
            if self.deck[i].isEvil():
                currentEvils.append(i)

        randomEvilIndex = random.choice(currentEvils)
        
        setDeck = set(range(len(self.deck)))
        setCurrentEvils = set(currentEvils)
        currentGood = list(setDeck - setCurrentEvils)
        randomGoodIndex = random.choice(currentGood)

        if self.isEvil() == False and self.isCorrupted() == False:
            allPositions = [randomEvilIndex, randomGoodIndex]
            position1 = random.choice(allPositions) 
            allPositions.remove(position1)
            position2 = allPositions[0]

            return f"#{position1} or #{position2} is a {self.deck[randomEvilIndex].getEvilName()}"
        
        else:
            currentGood.remove(randomGoodIndex)
            randomGoodIndex2 = random.choice(currentGood)
            return f"#{randomGoodIndex} or #{randomGoodIndex2} is a {self.deck[randomEvilIndex].getEvilName()}"
        
    def getDescription(self):
        return "Learn that 1 out of 2 characters is a specific Minion role"
    
    def getHint(self):
        return "If Lies: Both characters in my info are Good"
            
        