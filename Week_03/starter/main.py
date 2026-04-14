from fastapi import FastAPI
from database import create_db
from routers import categories, entities

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(categories.router)
app.include_router(entities.router)