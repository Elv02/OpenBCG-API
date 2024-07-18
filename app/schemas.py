from pydantic import BaseModel
from typing import Optional, Dict


class CardBase(BaseModel):
    name: str
    type: str
    cost: str
    attack: Optional[int] = None
    defense: Optional[int] = None
    text: Optional[str] = None
    art: Optional[Dict] = None
    faction: Optional[str] = None
    race: Optional[str] = None
    author: Optional[str] = None
    artist: Optional[str] = None
    rarity: Optional[str] = None
    series: Optional[str] = None
    additional_meta: Optional[Dict] = None


class CardCreate(CardBase):
    pass


class CardUpdate(CardBase):
    pass
