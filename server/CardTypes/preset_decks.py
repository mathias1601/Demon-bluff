from FortuneTeller import FortuneTeller
from Confessor import Confessor
from Knight import Knight
from Gemcrafter import Gemcrafter
from Bombardier import Bombardier
from Scout import Scout
from Oracle import Oracle
from Hunter import Hunter
from Judge import Judge
from Jester import Jester
from Knitter import Knitter
from Pooka import Pooka
from Bard import Bard
from PlagueDoctor import PlaugeDoctor
from Minion import Minion

all_preset_decks = [
    
]


evil1 = Bombardier(1, None, False, False, False, True)
evil2 = Hunter(6, None, False, False, False, True)
    
preset_deck1 = [
    Gemcrafter(0, None, True, False, False, False),
    Minion(evil1),
    Oracle(2, None, True, False, False, False),
    Jester(3, None, True, False, False, False),
    Scout(4, None, True, False, False, False),
    PlaugeDoctor(5, None, True, False, False, False),
    Minion(evil2),
]

# Assign the deck reference to all cards
for card in preset_deck1:
    card.assignDeck(preset_deck1)

all_preset_decks.append(preset_deck1)





evil1 = Bombardier(1, None, False, False, False, True)
evil2 = Judge(6, None, False, False, False, True)
    
preset_deck2 = [
    PlaugeDoctor(0, None, True, False, False, False),
    Minion(evil1),
    Gemcrafter(2, None, True, False, False, False),
    Jester(3, None, True, False, False, False),
    Knight(4, None, True, False, False, False),
    Knitter(5, None, True, False, False, False),
    Pooka(evil2),
    FortuneTeller(7, None, True, False, False, False),
    Bard(8, None, True, False, False, False),
]

# Assign the deck reference to all cards
for card in preset_deck2:
    card.assignDeck(preset_deck2)

all_preset_decks.append(preset_deck2)