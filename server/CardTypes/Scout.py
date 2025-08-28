from Card import Card
import random

class Scout(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Scout"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def getClosestEvil(self, startIndex):
        deck_size = len(self.deck)

        minDistanceClockwise = 0
        currentIndex = startIndex

        while self.deck[currentIndex].isEvil() == False or currentIndex == startIndex:
            minDistanceClockwise += 1
            currentIndex += 1
            if currentIndex >= deck_size:
                currentIndex = 0
            if minDistanceClockwise > deck_size:
                break
            
        minDistanceCounterClockwise = 0
        currentIndex = startIndex

        while self.deck[currentIndex].isEvil() == False or currentIndex == startIndex:
            minDistanceCounterClockwise += 1
            currentIndex -= 1

        if minDistanceClockwise < minDistanceCounterClockwise:
            return minDistanceClockwise
        else:
            return minDistanceCounterClockwise
        

    def reveal(self):

        currentEvils = []
        for i in range(len(self.deck)):
            if self.deck[i].isEvil():
                currentEvils.append(i)

        randomEvilIndex = random.choice(currentEvils)
        closestEvilDistance = self.getClosestEvil(randomEvilIndex) 

        if self.isEvil() == False and self.isCorrupted() == False:
            return f"{self.deck[randomEvilIndex].getEvilName()} is {closestEvilDistance} cards away from closest evil"
        
        else:
            # Calculate largest possible distance in circular deck
            if len(self.deck) % 2 == 0:
                largest_distance = len(self.deck) // 2
            else:
                largest_distance = (len(self.deck) - 1) // 2

            # Pick a random distance not equal to the closest
            random_distance = random.randint(1, largest_distance)
            while random_distance == closestEvilDistance:
                random_distance = random.randint(1, largest_distance)

            return f"{self.deck[randomEvilIndex].getEvilName()} is {random_distance} cards away from closest evil"

    
    def getDescription(self):
        return "Learn how far a specific Evil is to another closest Evil"
    