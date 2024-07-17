from fastapi import FastAPI
from app.routers import cards

app = FastAPI()

app.include_router(cards.router)

@app.get("/")
def read_root():
    return {"message": "Nothin' to see here!"}