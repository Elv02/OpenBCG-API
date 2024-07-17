from fastapi import APIRouter

router = APIRouter()

@router.get("/cards/")
def read_cards():
    return {"message": "List of cards"}

@router.get("/cards/{card_id}")
def read_card(card_id: int):
    return {"card_id": card_id, "message": "Details of a specific card"}

@router.post("/cards/")
def create_card(name: str):
    return {"name": name, "message": "Card created successfully"}

@router.put("/cards/{card_id}")
def update_card(card_id: int, name: str):
    return {"card_id": card_id, "name": name, "message": "Card updated successfully"}

@router.delete("/cards/{card_id}")
def delete_card(card_id: int):
    return {"card_id": card_id, "message": "Card deleted successfully"}
