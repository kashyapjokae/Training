from app.core.base import Base
from sqlalchemy import Column,Integer,String,Boolean 
class District_model(Base):
        __tablename__ = "district_master"
        district_id=Column(Integer,primary_key=True, index=True)
        district_name=Column(String(30),nullable=False)
        district_code=Column(String(3),nullable=True)
        is_active=Column(Boolean,nullable=False)