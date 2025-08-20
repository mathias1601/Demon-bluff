from typing import List
from pydantic import BaseModel
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
from PlagueDoctor import PlaugeDoctor
from Minion import Minion
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
active_deck = None


origins = [
    "http://localhost:3000",  # your React/Next.js frontend URL
    # you can add more allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allows these origins to access your API
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],    # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],    # allow all headers
)

@app.post("/create-deck")
def create_preset_deck1():

    evil1 = Hunter(6, None, False, False, False, True)
    evil2 = Bombardier(1, None, False, False, False, True)
    
    preset_deck1 = [
        Gemcrafter(0, None, True, False, False, False),
        Minion(evil2),
        Oracle(2, None, True, False, False, False),
        Jester(3, None, True, False, False, False),
        Scout(4, None, True, False, False, False),
        PlaugeDoctor(5, None, True, False, False, False),
        Minion(evil1),
    ]

    # Assign the deck reference to all cards
    for card in preset_deck1:
        card.assignDeck(preset_deck1)

    global active_deck
    active_deck = preset_deck1

    evilCount = 0

    """ Activate all start of game effects and count total evils """

    for card in active_deck:
        card.gameStart()
        if card.isEvil():
            evilCount += 1

    return { 
        "evilCount": evilCount,
        "deck": [
        {
            "positionIndex": card.getPositionIndex(),
            "name": card.getName(),
            "reveal": card.reveal(),
            "usage": card.getUsage(),
            "usageResult": None,
            "isRevealed": False,
            "isEvil": card.isEvil(),
            "executeEffect": card.execute()
        }
        for card in preset_deck1
    ]}


class UseCardRequest(BaseModel):
    cardIndex: int
    targets: List[int]  # Flexible number of target positions

@app.post("/use-card")
def use_card(request: UseCardRequest):
    card = active_deck[request.cardIndex]
    
    if card.getUsage() == 0:
        return

    # Call the card's `use` method dynamically with *args
    result = card.use(*request.targets)
    return {"usageResult": result}
