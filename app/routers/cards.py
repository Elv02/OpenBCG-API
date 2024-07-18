from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Card
from ..schemas import CardCreate, CardUpdate

router = APIRouter()


@router.get("/cards/")
def read_cards(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)  # noqa: B008
):
    cards = db.query(Card).offset(skip).limit(limit).all()
    return cards


@router.get("/cards/{card_id}")
def read_card(card_id: int, db: Session = Depends(get_db)):  # noqa: B008
    card = db.query(Card).filter(Card.id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.post("/cards/")
def create_card(card: CardCreate, db: Session = Depends(get_db)):  # noqa: B008
    db_card = Card(**card.model_dump())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


@router.put("/cards/{card_id}")
def update_card(
    card_id: int, card: CardUpdate, db: Session = Depends(get_db)  # noqa: B008
):
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    for key, value in card.model_dump().items():
        setattr(db_card, key, value)
    db.commit()
    db.refresh(db_card)
    return db_card


@router.delete("/cards/{card_id}")
def delete_card(card_id: int, db: Session = Depends(get_db)):  # noqa: B008
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    db.delete(db_card)
    db.commit()
    return {"message": "Card deleted successfully"}
