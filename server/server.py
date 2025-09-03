from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from server.preset_decks import all_preset_decks


app = FastAPI()
active_deck = None


origins = [
    "http://localhost:3000", 
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],    
    allow_headers=["*"],    
)

@app.post("/create-deck/{index}")
def create_preset_deck(index: int):
    global active_deck

    if index > len(all_preset_decks):
        raise HTTPException(
            status_code=400,
            detail=f"Index {index} is too large. Maximum allowed index is {len(all_preset_decks)}."
        )

    active_deck = all_preset_decks[index]

    evilCount = 0

    """ All cards that are present in the deck or can be present """
    allPresentCards = []

    """ Activate all start of game effects and count total evils """
    for card in active_deck:
        card.gameStart()
        if card.isEvil():
            evilCount += 1

    
    allPresentGoodCards = []
    for card in active_deck:
        name = card.getName()
        if name not in allPresentCards:
            allPresentGoodCards.append({
                "cardName": name,
                "cardDescription": card.getDescription(),
                "cardHint": card.getHint(),
            })
            allPresentCards.append(name)

    
    allPresentEvilCards = []
    for card in active_deck:
        name = card.getEvilName()
        if card.isEvil() and name not in allPresentCards:
            allPresentEvilCards.append({
                "cardName": name,
                "cardDescription": card.getEvilDescription(),
                "cardHint": card.getEvilHint(),
            })
            allPresentCards.append(name)

    return { 
        "evilCount": evilCount,
        "allPresentGoodCards": allPresentGoodCards,
        "allPresentEvilCards": allPresentEvilCards,
        "deck": [
            {
                "positionIndex": card.getPositionIndex(),
                "name": card.getName(),
                "reveal": card.reveal(),
                "usage": card.getUsage(),
                "usageResult": None,
                "isRevealed": False,
                "isEvil": card.isEvil(),
                "executeEffect": card.execute(),
            }
            for card in active_deck
        ]
    }

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
