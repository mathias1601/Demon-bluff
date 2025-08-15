from Card import Card
import random

class Hunter(Card):

    def __init__(self, positionIndex, deck, isVillager, isOutcast, isMinion, isDemon):
        self.name = "Hunter"
        super().__init__(positionIndex, deck, isVillager, isOutcast, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def getClosestEvil(self, startIndex):
        deck_size = len(self.deck)
        minDistance = None

        for i in range(deck_size):
            idx = (startIndex + i) % deck_size  # wrap around
            if self.deck[idx].getType() == "evil":
                minDistance = i
                break

        return minDistance

def reveal(self):
    closest_distance = self.getClosestEvil(self.positionIndex)

    self.revealed = True

    if self.villager:
        return f"I am {closest_distance} away from closest Evil"
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

