from fastapi import FastAPI
from sqlmodel import SQLModel
from routers import rentals

app = FastAPI()

@app.on_event("startup")
def on_startup():
    from routers.rentals import engine
    SQLModel.metadata.create_all(engine)

app.include_router(rentals.router)