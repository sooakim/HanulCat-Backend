import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class PetStatus(Base):
    __tablename__ = "pet_status"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    image_id = Column(Integer, ForeignKey("pet_image.id"))
    image = relationship("PetImage", back_populates="statuses")