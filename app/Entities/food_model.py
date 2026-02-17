from app.core.base import Base
from sqlalchemy import Column,Integer,String,Boolean 
class FastFood_model(Base):
        __tablename__ = "fastfood_master"
        id=Column(Integer,primary_key=True, index=True)
        name=Column(String(30),nullable=False)
        code=Column(String(3),nullable=True)
        is_active=Column(Boolean,nullable=False)