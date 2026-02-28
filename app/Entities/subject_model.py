from app.core.base import Base
from sqlalchemy import Column,Integer,String
class Subject_model(Base):
        __tablename__ = "Subject"
        id=Column(Integer,primary_key=True, index=True)
        name=Column(String(30),nullable=False)
        code=Column(String(3),nullable=True)