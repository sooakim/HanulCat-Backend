from bcrypt import hashpw, checkpw, gensalt
from fastapi import APIRouter

from database.dao import get_user_by_password
from routers.auth import response, request

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post('/login', response_model=response.LoginResponse)
async def login(body: request.LoginRequest):
    hashedPassword = hashpw(body.password, salt=gensalt())
    user = get_user_by_password(email=body.email, password=hashedPassword)
    return response.LoginResponse(id=user.id, email=user.email, name=user.name, blocked=user.blocked)
