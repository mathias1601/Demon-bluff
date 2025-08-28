from Card import Card
import random

class Hunter(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Hunter"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def getClosestEvil(self, startIndex):
    
        for i in range(len(self.deck)):
            left = startIndex - i
            right = startIndex + i

            if left >= 0 and self.deck[left].isEvil():
                return i
            if right < len(self.deck) and self.deck[right].isEvil():
                return i

    def reveal(self):
        closest_distance = self.getClosestEvil(self.positionIndex)

        self.revealed = True

        if self.isEvil() == False and self.isCorrupted() == False:
            return f"I am {closest_distance} cards away from closest Evil"
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

            return f"I am {random_distance} away from closest Evil"

    def getDescription(self):
        return "Learn how far I am from the nearest Evil"