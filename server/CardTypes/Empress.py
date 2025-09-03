from server.CardTypes.Card import Card
import random

class Empress(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Empress"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):

        allEvils = []
        for i in range(len(self.deck)):
            if self.deck[i].isEvil():
                allEvils.append(i)

        randomEvil = random.choice(allEvils)

        allGood = []
        for i in range(len(self.deck)):
            if self.deck[i].isEvil() == False:
                allGood.append(i)

        randomGood1 = random.choice(allGood)
        allGood.remove(randomGood1)
        randomGood2 = random.choice(allGood)

        if self.isEvil() == False and self.isCorrupted() == False:
            allChoices = [randomEvil, randomGood1, randomGood2]
            randomChoice1 = random.choice(allChoices)
            allChoices.remove(randomChoice1)
            randomChoice2 = random.choice(allChoices)
            randomChoice3 = allChoices[0]

            return f"One is evil: #{randomChoice1}, #{randomChoice2} or #{randomChoice3}"
        

        else:
            
            allGood.remove(randomGood2)
            randomGood3 = random.choice(allGood)

            allChoices = [randomGood1, randomGood2, randomGood3]
            randomChoice1 = random.choice(allChoices)
            allChoices.remove(randomChoice1)
            randomChoice2 = random.choice(allChoices)
            randomChoice3 = allChoices[0]

            return f"One is evil: #{randomChoice1}, #{randomChoice2} or #{randomChoice3}"

    def getDescription(self):
        return "Learn 3 characters. Only 1 is Evil"
    
    def getHint(self):
        return "If Lies: All characters in my info are Good"