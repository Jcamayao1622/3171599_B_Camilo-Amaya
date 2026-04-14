from sqlmodel import SQLModel, Field
from enum import Enum
from datetime import datetime

class RentalStatus(str, Enum):
    REQUESTED = "requested"
    APPROVED = "approved"
    IN_USE = "in_use"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class RentalOrder(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    rental_code: str
    machinery_id: int
    client_name: str
    days: int
    total_price: float
    status: RentalStatus = RentalStatus.REQUESTED
    requested_by: str
    notes: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    approved_at: datetime | None = None
    completed_at: datetime | None = None