from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

from database.database import Base

class PetStatus(Base):
    __tablename__ = "pet_status"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    deleted = Column(Boolean, default=False)
    created_at = Column(Date)
    updated_at = Column(Date)
    image = relationship("pet", back_populates="statuses")