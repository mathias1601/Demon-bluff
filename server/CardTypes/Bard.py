from server.CardTypes.Card import Card
import random

class Bard(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Bard"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def getClosestCorrupted(self, startIndex):
        deck_size = len(self.deck)

        minDistanceClockwise = 0
        currentIndex = startIndex

        while self.deck[currentIndex].isCorrupted() == False or currentIndex == startIndex:
            minDistanceClockwise += 1
            currentIndex += 1
            if currentIndex >= deck_size:
                currentIndex = 0
            if minDistanceClockwise > deck_size:
                break
            
        minDistanceCounterClockwise = 0
        currentIndex = startIndex

        while self.deck[currentIndex].isCorrupted() == False or currentIndex == startIndex:
            minDistanceCounterClockwise += 1
            currentIndex -= 1

        if minDistanceClockwise < minDistanceCounterClockwise:
            return minDistanceClockwise
        else:
            return minDistanceCounterClockwise
        

    def reveal(self):

        closest_distance = self.getClosestCorrupted(self.positionIndex)

        self.revealed = True

        if self.isEvil() == False and self.isCorrupted() == False:
            return f"I am {closest_distance} cards away from closest Corrupted"
        else:
            # Calculate largest possible distance in circular deck
            if len(self.deck) % 2 == 0:
                largest_distance = len(self.deck) // 2
            else:
                largest_distance = (len(self.deck) - 1) // 2

            # Pick a random distance not equal to the closest
            random_distance = random.randint(1, largest_distance)
            while random_distance == closest_distance:
                random_distance = random.randint(1, largest_distance)

            return f"I am {random_distance} away from closest Corrupted"
        
    def getDescription(self):
        return "Learn how far away I am from closest Corrupted character"