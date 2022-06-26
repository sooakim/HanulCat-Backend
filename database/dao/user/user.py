from sqlite3 import Date

from sqlalchemy import and_
from sqlalchemy.orm import Session

from database.entity import *
from dependencies.password.password import check_hash, create_hash


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_password(db: Session, email: str, password: str):
    user = db.query(User).filter(and_(User.email == email)).first()
    if check_hash(user.password, password):
        return user
    else:
        raise Exception()


def create_user(db: Session, email: str, name: str, password: str):
    user = User(email=email, name=name, password=create_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
