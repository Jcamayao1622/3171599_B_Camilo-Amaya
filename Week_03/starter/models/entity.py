from sqlmodel import SQLModel, Field

class Machinery(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sku: str
    name: str
    category_id: int
    brand: str
    model: str
    year: int
    price_per_day: float
    availability: bool