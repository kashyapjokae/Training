from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import SessionLocal
from app.Entities.department_model import Department
from app.dtos.department_dto import DepartmentCreateDTO, DepartmentResponseDTO

router = APIRouter(prefix="/departments", tags=["Departments"])

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE Department
@router.post("/", response_model=DepartmentResponseDTO)
def create_department(department: DepartmentCreateDTO, db: Session = Depends(get_db)):
    db_department = Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

# GET All Departments
@router.get("/", response_model=List[DepartmentResponseDTO])
def get_departments(db: Session = Depends(get_db)):
    departments = db.query(Department).all()
    return departments