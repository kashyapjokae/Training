from sqlalchemy import Column,Integer,String
from app.core.base import Base

class Student(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name=Column(String,nullable=False)
    roll_no=Column(Integer,unique=True,nullable=False)
    image_path=Column(String)
    age = Column(Integer)
    course = Column(String)
