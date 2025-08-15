from Card import Card
import random

class Lovers(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Lovers"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):
        
        if self.villager:
            if self.deck[self.positionIndex - 1].getType() == "evil" and self.deck[self.positionIndex + 1].getType() == "evil":
                return "There are 2 evil(s) adjecent to me"
            elif self.deck[self.positionIndex - 1] == "demon" or self.deck[self.positionIndex + 1] == "demon":
                return "There is 1 evil(s) adjecent to me"
            else:
                return "There are 0 evil(s) next to me"
        
        if self.minion or self.demon:
            if self.deck[self.positionIndex - 1] == "evil" and self.deck[self.positionIndex + 1] == "evil":
                return "There is 1 evil adjecent to me"
            elif self.deck[self.positionIndex - 1] == "evil" or self.deck[self.positionIndex + 1] == "evil":
                randNum = random.choice([0, 2])
                return f"There are ${randNum} evil(s) adjecent to me"
            else:
                return "There is 1 evil(s) next to me"

