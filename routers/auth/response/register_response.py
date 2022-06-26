from pydantic import BaseModel


class RegisterResponse(BaseModel):
    id: int
    email: str
    name: str
    blocked: bool