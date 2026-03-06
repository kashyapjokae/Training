from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.base import Base

class Award(Base):
    __tablename__ = "awards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer)

    movie_id = Column(Integer, ForeignKey("movies.id"))

    movie = relationship("Movie", back_populates="awards")