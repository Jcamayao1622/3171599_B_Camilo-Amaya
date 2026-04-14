from pydantic import BaseModel
from models import RentalStatus

class RentalResponse(BaseModel):
    id: int
    rental_code: str
    status: RentalStatus

class RentalDetailResponse(RentalResponse):
    client_name: str
    days: int
    total_price: float
    notes: str | None