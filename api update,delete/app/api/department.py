from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.entities.department_entity import Department
from app.dtos.department_dto import DepartmentUpdate

router = APIRouter()

# UPDATE API
@router.put("/department/{id}")
def update_department(id: int, dept: DepartmentUpdate, db: Session = Depends(get_db)):
    department = db.query(Department).filter(Department.id == id).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    department.name = dept.name
    department.description = dept.description

    db.commit()
    db.refresh(department)

    return department


# DELETE API
@router.delete("/department/{id}")
def delete_department(id: int, db: Session = Depends(get_db)):
    department = db.query(Department).filter(Department.id == id).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    db.delete(department)
    db.commit()

    return {"message": "Department deleted successfully"}