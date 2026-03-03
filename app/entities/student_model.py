from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    roll_no = Column(String, unique=True, nullable=False)
    image_path = Column(String, nullable=False)