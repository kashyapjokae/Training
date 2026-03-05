from app.core.base import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    roll_no = Column(Integer)
    image_path = Column(String(255))