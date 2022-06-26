import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Pet(Base):
    __tablename__ = "pet"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="pets")

    images = relationship("PetImage", back_populates="pet")
