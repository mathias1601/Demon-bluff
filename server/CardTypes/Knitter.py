from Card import Card
import random

class Knitter(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Knitter"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name

    def reveal(self):

        amountOfPairs = 0

        maxEvils = 0
        for card in self.deck:
            if card.isEvil():
                maxEvils += 1 

        for i in range(len(self.deck) - 1):
            if self.deck[i].isEvil() and self.deck[i + 1].isEvil():
                amountOfPairs += 1

        if self.isEvil() == False and self.isCorrupted() == False:
            if amountOfPairs == 1:
                 return f"There is only {amountOfPairs} pair of evil"
            return f"There are {amountOfPairs} pairs of evil"
        
        else:

            possiblePairs = list(range(maxEvils))
            randomAmountPairs = random.choice(possiblePairs)

            if amountOfPairs == 1:
                 return f"There is only {randomAmountPairs} pair of evil"
            return f"There are {randomAmountPairs} pairs of evil"
            