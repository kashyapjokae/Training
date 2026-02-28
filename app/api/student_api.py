from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db 

from app.Entities.student import student as Student_entity
from app.dtos.student_dto import StudentCreate, StudentResponse, StudentUpdate
router = APIRouter(prefix="/Student", tags=["Student"])

@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = Student_entity(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/", response_model=List[StudentResponse])
def get_students(db: AsyncSession = Depends(get_db)):
    return db.query(Student_entity).all()

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: AsyncSession = Depends(get_db)):
    db_student = db.query(Student_entity).filter(Student_entity.id == student_id).first()
    
    if not db_student: 
        raise HTTPException(status_code=404, detail="Student not found")

    db_student.name = student.name
    db_student.age = student.age
    db_student.course = student.course
    
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    db_student = db.query(Student_entity).filter(Student_entity.id == student_id).first()                 
   
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
     
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}

@app.patch("/students/{student_id}", response_model=StudentResponse)
def update_student_partial(student_id: int, student_data: StudentUpdate, db: AsyncSession = Depends(get_db)):
    student_obj = db.query(Student_entity).filter(Student_entity.id == student_id).first()

    if not student_obj:
        raise HTTPException(status_code=404, detail="Student not found")
     
   
    update_data = student_data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student_obj, key, value)

    db.commit()
    db.refresh(student_obj)
    return student_obj
