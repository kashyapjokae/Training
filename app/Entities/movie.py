from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.base import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    actor_id = Column(Integer, ForeignKey("actors.id"), nullable=False)

    actor = relationship("Actor", back_populates="movies")
    awards = relationship("Award", back_populates="movie")