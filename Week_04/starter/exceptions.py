from fastapi import HTTPException

class RentalNotFoundError(HTTPException):
    def __init__(self, rental_id: int):
        super().__init__(
            status_code=404,
            detail=f"Rental {rental_id} not found"
        )

class InvalidTransitionError(HTTPException):
    def __init__(self, current: str, target: str):
        super().__init__(
            status_code=400,
            detail=f"Cannot transition from {current} to {target}"
        )