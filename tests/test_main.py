import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module", autouse=True)
def clean_up():
    yield
    if os.path.exists("test.db"):
        os.remove("test.db")


def test_read_root(setup_database):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_card(setup_database):
    response = client.post(
        "/cards/",
        json={
            "name": "Test Card",
            "type": "Spell",
            "cost": "2G",
            "attack": 2,
            "defense": 2,
            "text": "This is a test card.",
            "art": {},
            "faction": "Test",
            "race": "Test",
            "author": "Author",
            "artist": "Artist",
            "rarity": "Common",
            "series": "Test",
            "additional_meta": {},
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Card"
    assert data["type"] == "Spell"
