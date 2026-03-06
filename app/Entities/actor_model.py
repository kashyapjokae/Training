from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.base import Base

class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    movies = relationship("Movie", back_populates="actor")