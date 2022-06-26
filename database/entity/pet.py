from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

from database.database import Base

class Pet(Base):
    __tablename__ = "pet"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(Date)
    updated_at = Column(Date)
    user = relationship("user", back_populates="pets")
    images = relationship("pet_image", back_populates="pet")
