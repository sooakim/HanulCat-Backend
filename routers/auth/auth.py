from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from database.dao.user import get_user_by_password, create_user
from dependencies.password import password
from routers.auth import response, request

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post('/login', response_model=response.LoginResponse, description="이메일로 로그인")
def login(body: request.LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_password(db, email=body.email, password=password.create_hash(body.password))
    return response.LoginResponse(id=user.id, email=user.email, name=user.name, blocked=user.blocked)


@router.post('/register', response_model=response.RegisterResponse, description="이메일로 회원가입")
def register(body: request.RegisterRequest, db: Session = Depends(get_db)):
    user = create_user(db, email=body.email, name=body.name, password=password.create_hash(body.password))
    return response.LoginResponse(id=user.id, email=user.email, name=user.name, blocked=user.blocked)
