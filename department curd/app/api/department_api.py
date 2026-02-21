from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.Entities.department_model import Department
from app.dtos.department_dto import DepartmentCreateDTO

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/")
def create_department(department: DepartmentCreateDTO, db: Session = Depends(get_db)):
    db_department = Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

# READ ALL
@router.get("/")
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()

# READ BY ID
@router.get("/{id}")
def get_department(id: int, db: Session = Depends(get_db)):
    department = db.query(Department).filter(Department.id == id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

# UPDATE
@router.put("/{id}")
def update_department(id: int, department: DepartmentCreateDTO, db: Session = Depends(get_db)):
    db_department = db.query(Department).filter(Department.id == id).first()
    if not db_department:
        raise HTTPException(status_code=404, detail="Department not found")
    db_department.name = department.name
    db.commit()
    db.refresh(db_department)
    return db_department

# DELETE
@router.delete("/{id}")
def delete_department(id: int, db: Session = Depends(get_db)):
    db_department = db.query(Department).filter(Department.id == id).first()
    if not db_department:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(db_department)
    db.commit()
    return {"message": "Department deleted successfully"}
