from sqlalchemy import Column,Integer,String,ForeignKey
from app.core.base import Base

class Award(Base):
    __tablename__="awards" 
    id=Column(Integer,primary_key=True,index=True)
    award_name=Column(String,nullable=False)
    movie_id=Column(Integer,ForeignKey("movies.id"),nullable=False)

