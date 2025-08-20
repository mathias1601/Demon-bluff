from Card import Card
import random

class Englightened(Card):

    def __init__(self, positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon):
        self.name = "Enlightened"
        super().__init__(positionIndex, deck, isVillager, isCorrupted, isMinion, isDemon)

    def getName(self):
        return self.name
    
    def reveal(self):
        deck_size = len(self.deck)

        # Clockwise distance
        cw_distance = None
        for i in range(deck_size):
            idx = (self.positionIndex + i) % deck_size
            if self.deck[idx].isEvil():
                cw_distance = i
                break

        # Counter-clockwise distance
        ccw_distance = None
        for i in range(deck_size):
            idx = (self.positionIndex - i) % deck_size
            if self.deck[idx].isEvil():
                ccw_distance = i
                break
        
        if self.isEvil() == False and not self.corrupted:

            if cw_distance < ccw_distance:
                return "The closest evil is clockwise"
            elif ccw_distance < cw_distance:
                return "The closest evil is counterclockwise"
            else:
                return "The closest evil is equidistant"
            
        else:

            allAnswers = ["The closest evil is clockwise", "The closest evil is counterclockwise", "The closest evil is equidistant"]

            if cw_distance > ccw_distance:
                allAnswers.remove("The closest evil is clockwise")
                randomAnswer = random.choice(allAnswers)
                return randomAnswer
            elif ccw_distance > cw_distance:
                allAnswers.remove("The closest evil is counterclockwise")
                randomAnswer = random.choice(allAnswers)
                return randomAnswer
            else:
                allAnswers.remove("The closest evil is equidistant")
                randomAnswer = random.choice(allAnswers)
                return randomAnswer

