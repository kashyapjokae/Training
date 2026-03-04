from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db 
from app.core.database import engine 
from app.Entities.student import Student as Student_entity
from app.dtos.student_dto import StudentCreate, StudentResponse, StudentUpdate
from sqlalchemy import select
from fastapi import UploadFile, File, Form
import shutil
import os



router = APIRouter(prefix="/Student", tags=["Student"])
@router.post("/students", response_model=StudentResponse)
async def create_student(
    first_name: str = Form(...),
    last_name: str = Form(...),
    roll_no: int = Form(...),
    age: int = Form(...),
    course: str = Form(...),
    image: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):  
    upload_dir='uploads'   
    os.makedirs(upload_dir,exist_ok=True)
    file_path=os.path.join(upload_dir,image.filename)
    with open(file_path,"wb")as buffer:
        shutil.copyfileobj(image.file,buffer)
    
    new_student = Student_entity(
        first_name=first_name,
        last_name=last_name,
        roll_no=roll_no,
        age=age,
        course=course,
        image_path=file_path
    )
    db.add(new_student)
    await  db.commit()
    await  db.refresh(new_student)
    return new_student 

@router.get("/students/", response_model=list[StudentResponse])
async def get_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student_entity))
    students = result.scalars().all()
    return students

@router.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(
    student_id: int,
    first_name: str = Form(...),
    last_name: str = Form(...),
    roll_no: int = Form(...),
    age: int = Form(...),
    course: str = Form(...),
    image: UploadFile = File(None),  # optional
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Student_entity).where(Student_entity.id == student_id))
    db_student = result.scalar_one_or_none()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    # optional image update
    if image:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, image.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        db_student.image_path = file_path

    db_student.first_name = first_name
    db_student.last_name = last_name
    db_student.roll_no = roll_no
    db_student.age = age
    db_student.course = course

    await db.commit()
    await db.refresh(db_student)
    return db_student

@router.delete("/students/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student_entity).where(Student_entity.id == student_id))
    db_student = result.scalar_one_or_none()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    # delete image from folder (optional)
    if db_student.image_path and os.path.exists(db_student.image_path):
        os.remove(db_student.image_path)

    await db.delete(db_student)
    await db.commit()
    return {"message": "Student deleted successfully"}

@router.patch("/students/{student_id}", response_model=StudentResponse)
async def update_student_partial(
    student_id: int,
    student: StudentUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Student_entity).where(Student_entity.id == student_id))
    student_obj = result.scalar_one_or_none()

    if not student_obj:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.dict(exclude_unset=True).items():
        setattr(student_obj, key, value)

    await db.commit()
    await db.refresh(student_obj)
    return student_obj