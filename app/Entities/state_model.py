from app.core.base import Base
from sqlalchemy import Column,Integer,String 
class mummy_master(Base): 
        __tablename__ = "state_master"
        id=Column(Integer,primary_key=True, index=True)
        name=Column(String(30),nullable=False)
        code=Column(String(3),nullable=True)
        
