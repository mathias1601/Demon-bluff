from typing import List
from pydantic import BaseModel
from FortuneTeller import FortuneTeller
from Confessor import Confessor
from Knight import Knight
from Gemcrafter import Gemcrafter
from Judge import Judge
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

    evil1 = Confessor(2, None, False, False, False, True)
    evil2 = Gemcrafter(3, None, False, False, True, False)
    
    preset_deck1 = [
        Knight(0, None, True, False, False, False),
        FortuneTeller(1, None, True, False, False, False),
        Minion(evil1),
        Minion(evil2),
        Judge(4, None, True, False, False, False),
        Judge(5, None, True, False, False, False),
        Gemcrafter(6, None, True, False, False, False),
    ]

    # Assign the deck reference to all cards
    for card in preset_deck1:
        card.assignDeck(preset_deck1)

    global active_deck
    active_deck = preset_deck1

    evilCount = 0

    for card in active_deck:
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
