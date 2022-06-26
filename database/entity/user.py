from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship

from database.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    password = Column(String, index=True)
    deleted = Column(Boolean, default=False)
    blocked = Column(Boolean, default=False)
    created_at = Column(Date)
    updated_at = Column(Date)
    pets = relationship("pet", back_populates="user")