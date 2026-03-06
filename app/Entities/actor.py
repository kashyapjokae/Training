from sqlalchemy import Column,String,Integer
from app.core.base import Base

class Actor(Base):
    __tablename__="actors"

    id = Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
   