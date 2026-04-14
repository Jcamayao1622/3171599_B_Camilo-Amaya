from fastapi import APIRouter
from sqlmodel import Session, select, create_engine
from models import RentalOrder, RentalStatus
from schemas.request import RentalCreateRequest
from schemas.response import RentalResponse
from exceptions import RentalNotFoundError, InvalidTransitionError

router = APIRouter(prefix="/rentals", tags=["Rentals"])

engine = create_engine("sqlite:///database.db")

def get_session():
    with Session(engine) as session:
        yield session
 
@router.post("/", response_model=RentalResponse, status_code=201)
def create_rental(data: RentalCreateRequest):
    with Session(engine) as session:
        rental = RentalOrder(**data.dict())
        session.add(rental)
        session.commit()
        session.refresh(rental)
        return rental        

@router.get("/{id}", response_model=RentalResponse)
def get_rental(id: int):
    with Session(engine) as session:
        rental = session.get(RentalOrder, id)

        if not rental:
            raise RentalNotFoundError(id)

        return rental        
        
@router.post("/{id}/approve")
def approve(id: int):
    with Session(engine) as session:
        rental = session.get(RentalOrder, id)

        if not rental:
            raise RentalNotFoundError(id)

        if rental.status != RentalStatus.REQUESTED:
            raise InvalidTransitionError(rental.status, "approved")

        rental.status = RentalStatus.APPROVED
        session.commit()
        return rental
    
@router.post("/{id}/start")
def start(id: int):
    with Session(engine) as session:
        rental = session.get(RentalOrder, id)

        if rental.status != RentalStatus.APPROVED:
            raise InvalidTransitionError(rental.status, "in_use")

        rental.status = RentalStatus.IN_USE
        session.commit()
        return rental
    
@router.post("/{id}/complete")
def complete(id: int):
    with Session(engine) as session:
        rental = session.get(RentalOrder, id)

        if rental.status != RentalStatus.IN_USE:
            raise InvalidTransitionError(rental.status, "completed")

        rental.status = RentalStatus.COMPLETED
        session.commit()
        return rental
    
@router.post("/{id}/cancel")
def cancel(id: int):
    with Session(engine) as session:
        rental = session.get(RentalOrder, id)

        if rental.status == RentalStatus.COMPLETED:
            raise InvalidTransitionError(rental.status, "cancelled")

        rental.status = RentalStatus.CANCELLED
        session.commit()
        return rental
    
            
                