from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
Base = declarative_base()
class StateMaster(Base): 
        __tablename__ = "state_master"
        id=Column(Integer,primary_key=True, index=True)
        name=Column(String(30),nullable=False)
        code=Column(String(3),nullable=True)
        
