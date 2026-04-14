from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models.category import MachineryCategory
from database import engine

router = APIRouter(prefix="/categories", tags=["Categories"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/")
def get_categories(session: Session = Depends(get_session)):
    return session.exec(select(MachineryCategory)).all()

@router.post("/")
def create_category(category: MachineryCategory, session: Session = Depends(get_session)):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category