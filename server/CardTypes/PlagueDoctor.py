from Card import Card
import random

class PlaugeDoctor(Card):

    def __init__(self, positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon):
        self.name = "Plague Doctor"
        super().__init__(positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon)

    def getName(self):
        return self.name

    def gameStart(self):
        allOtherCards = self.deck[:self.positionIndex] + self.deck[self.positionIndex+1:]
        randomCard = random.choice(allOtherCards)

        while randomCard.isEvil():
            randomCard = random.choice(allOtherCards)

        randomCard.corrupted = True

    def use(self, position):

        if self.isEvil() == False and self.corrupted == False:

            if self.deck[position].isCorrupted():
                
                allEvils = []
                for i in range(len(self.deck)):
                    if self.deck[i].isEvil():
                        allEvils.append(i)

                randomEvil = random.choice(allEvils)

                return f"#{position} is corrupted, #{randomEvil} is evil"
            
            else:
                return f"#{position} is not corrupted"
        
        else:
            """ 1: Villager is corrupted, but wrong evil is given
            2: Villager is corrupted, but plague doctor says it is not
            3: Villager is not corrupted, and wrong evil is given """ 

            allGood = []
            for i in range(len(self.deck)):
                if self.deck[i].isEvil() == False:
                    allGood.append(i)

            randomGood = random.choice(allGood)

            if self.deck[position].isCorrupted():

                options = [1, 2]
                randomOption = random.choice(options)

                if randomOption == 1:

                    return f"#{position} is corrupted, #{randomGood} is evil"
                
                else:

                    return f"#{position} is not corrupted"
                
            else:

                 return f"#{position} is corrupted, #{randomGood} is evil"
                

        
    def getUsage(self):
        return 1