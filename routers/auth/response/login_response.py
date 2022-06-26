from pydantic import BaseModel


class LoginResponse(BaseModel):
    id: int
    email: str
    name: str
    blocked: bool