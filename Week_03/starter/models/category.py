from sqlmodel import SQLModel, Field

class MachineryCategory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    code: str
    name: str
    description: str
    requires_operator: bool