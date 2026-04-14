from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models.entity import Machinery
from database import engine

router = APIRouter(prefix="/machinery", tags=["Machinery"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/")
def get_machinery(
    brand: str = None,
    price_gte: float = None,
    price_lte: float = None,
    year_gte: int = None,
    availability: bool = None,
    search: str = None,
    sort_by: str = "price_per_day",
    order: str = "asc",
    session: Session = Depends(get_session)
):
    query = select(Machinery)

    if brand:
        query = query.where(Machinery.brand == brand)

    if price_gte:
        query = query.where(Machinery.price_per_day >= price_gte)

    if price_lte:
        query = query.where(Machinery.price_per_day <= price_lte)

    if year_gte:
        query = query.where(Machinery.year >= year_gte)

    if availability is not None:
        query = query.where(Machinery.availability == availability)

    if search:
        query = query.where(
            (Machinery.name.contains(search)) |
            (Machinery.model.contains(search))
        )

    if order == "desc":
        query = query.order_by(getattr(Machinery, sort_by).desc())
    else:
        query = query.order_by(getattr(Machinery, sort_by))

    return session.exec(query).all()

@router.post("/")
def create_machinery(machinery: Machinery, session: Session = Depends(get_session)):
    session.add(machinery)
    session.commit()
    session.refresh(machinery)
    return machinery