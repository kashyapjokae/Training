import os
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.entities.student_model import Student

router = APIRouter(prefix="/students", tags=["Students"])

UPLOAD_FOLDER = "app/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


#  CREATE STUDENT
@router.post("/")
def create_student(
    firstname: str = Form(...),
    lastname: str = Form(...),
    roll_no: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = f"{UPLOAD_FOLDER}/{image.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(image.file.read())

    student = Student(
        firstname=firstname,
        lastname=lastname,
        roll_no=roll_no,
        image_path=file_path
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return {"message": "Student created", "id": student.id}


#  GET ALL STUDENTS
@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


#  GET STUDENT BY ID
@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


#  UPDATE STUDENT
@router.put("/{student_id}")
def update_student(
    student_id: int,
    firstname: str = Form(None),
    lastname: str = Form(None),
    roll_no: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if firstname:
        student.firstname = firstname

    if lastname:
        student.lastname = lastname

    if roll_no:
        student.roll_no = roll_no

    if image:
        file_path = f"{UPLOAD_FOLDER}/{image.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(image.file.read())
        student.image_path = file_path

    db.commit()
    db.refresh(student)

    return {"message": "Student updated successfully"}


#  DELETE STUDENT
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}