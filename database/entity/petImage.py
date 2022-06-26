from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

from database.database import Base

class PetImage(Base):
    __tablename__ = "pet_image"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    deleted = Column(Boolean, default=False)
    created_at = Column(Date)
    updated_at = Column(Date)
    pet = relationship("pet", back_populates="images")
    statuses = relationship("pet_status", back_populates="image")