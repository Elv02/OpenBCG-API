from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import engine
from .models import Base
from .routers import cards


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Perform cleanup actions if any


app = FastAPI(lifespan=lifespan)

app.include_router(cards.router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
