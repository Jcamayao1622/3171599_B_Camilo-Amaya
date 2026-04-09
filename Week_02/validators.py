import re
from pydantic import field_validator
from models import Machine

class MachineValidator(Machine):

    @field_validator("code")
    def validate_code(cls, v: str):
        if not re.match(r"^[A-Z]{3}-\d{3}$", v):
            raise ValueError("Code must be format ABC-123")
        return v

    @field_validator("location")
    def validate_location(cls, v: str):
        if not re.match(r"^[A-Z]-\d{2}$", v):
            raise ValueError("Location must be format A-01")
        return v