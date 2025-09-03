from server.CardTypes.FortuneTeller import FortuneTeller
from server.CardTypes.Confessor import Confessor
from server.CardTypes.Knight import Knight
from server.CardTypes.Gemcrafter import Gemcrafter
from server.CardTypes.Bombardier import Bombardier
from server.CardTypes.Scout import Scout
from server.CardTypes.Oracle import Oracle
from server.CardTypes.Hunter import Hunter
from server.CardTypes.Judge import Judge
from server.CardTypes.Jester import Jester
from server.CardTypes.Knitter import Knitter
from server.CardTypes.Pooka import Pooka
from server.CardTypes.Bard import Bard
from server.CardTypes.PlagueDoctor import PlagueDoctor
from server.CardTypes.Minion import Minion

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
    PlagueDoctor(5, None, True, False, False, False),
    Minion(evil2),
]

# Assign the deck reference to all cards
for card in preset_deck1:
    card.assignDeck(preset_deck1)

all_preset_decks.append(preset_deck1)





evil1 = Bombardier(1, None, False, False, False, True)
evil2 = Judge(6, None, False, False, False, True)
    
preset_deck2 = [
    PlagueDoctor(0, None, True, False, False, False),
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