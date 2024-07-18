from sqlalchemy import Column, Integer, String, SmallInteger, JSON
from .database import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    cost = Column(String)
    attack = Column(SmallInteger)
    defense = Column(SmallInteger)
    text = Column(String)
    art = Column(JSON)
    faction = Column(String)
    race = Column(String)
    author = Column(String)
    artist = Column(String)
    rarity = Column(String)
    series = Column(String)
    additional_meta = Column(JSON)
