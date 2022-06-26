import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class PetImage(Base):
    __tablename__ = "pet_image"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    pet_id = Column(Integer, ForeignKey("pet.id"))
    pet = relationship("Pet", back_populates="images")

    statuses = relationship("PetStatus", back_populates="image")