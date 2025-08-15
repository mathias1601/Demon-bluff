from Card import Card
import random

class Gemcrafter(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Gemcrafter"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):
            
        villagerList = []
        evilList = []
        
        for card in self.deck:
            if card.getType() == "evil":
                evilList.append(card)
            else:
                villagerList.append(card)

        randomCard = None

        if self.villager:
            randomCard = random.choice(villagerList)
        else:
            randomCard = random.choice(villagerList)
        
        self.revealed = True
        return f"#{randomCard.getPositionIndex()}, {randomCard.getName()} is good"
    
            
