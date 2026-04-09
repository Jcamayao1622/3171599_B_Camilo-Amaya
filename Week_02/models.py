from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from decimal import Decimal

class Machine(BaseModel):
    id: int
    code: str
    name: str
    description: Optional[str] = None
    type: str
    power: int = Field(ge=0)
    price: Decimal = Field(gt=0)
    location: str
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None