from sqlite3 import Date

from sqlalchemy.orm import Session

from database.entity import User


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_password(db: Session, email: str, password: str):
    return db.query(User).filter(User.email == email and password == password).first()

def create_user(db: Session, email: str, name: str, password: str):
    user = User(email=email, name=name, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user