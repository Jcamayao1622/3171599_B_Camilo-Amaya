from pydantic import BaseModel

class RentalCreateRequest(BaseModel):
    rental_code: str
    machinery_id: int
    client_name: str
    days: int
    total_price: float
    requested_by: str
    notes: str | None = None