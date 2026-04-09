from fastapi import FastAPI, HTTPException
from typing import List
from models import Machine
from database import db
from datetime import datetime

app = FastAPI(title="Agrotech CRUD API")

# CREATE
@app.post("/machines/")
def create_machine(machine: Machine):
    if any(m.code == machine.code for m in db):
        raise HTTPException(status_code=400, detail="Code must be unique")

    machine.created_at = datetime.now()
    db.append(machine)
    return machine

# READ ALL
@app.get("/machines/")
def get_machines(skip: int = 0, limit: int = 10):
    return db[skip: skip + limit]

# READ ONE
@app.get("/machines/{id}")
def get_machine(id: int):
    for m in db:
        if m.id == id:
            return m
    raise HTTPException(status_code=404, detail="Machine not found")

# SEARCH UNIQUE
@app.get("/machines/by-code/{code}")
def get_by_code(code: str):
    for m in db:
        if m.code == code:
            return m
    raise HTTPException(status_code=404, detail="Not found")

# UPDATE
@app.patch("/machines/{id}")
def update_machine(id: int, data: dict):
    for m in db:
        if m.id == id:
            for key, value in data.items():
                setattr(m, key, value)
            m.updated_at = datetime.now()
            return m
    raise HTTPException(status_code=404, detail="Not found")

# DELETE
@app.delete("/machines/{id}")
def delete_machine(id: int):
    for i, m in enumerate(db):
        if m.id == id:
            db.pop(i)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Not found")