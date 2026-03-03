import os
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.entities.student_model import Student

router = APIRouter(prefix="/students", tags=["Students"])

UPLOAD_FOLDER = "app/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@router.post("/create")
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

    new_student = Student(
        firstname=firstname,
        lastname=lastname,
        roll_no=roll_no,
        image_path=file_path
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student created successfully",
        "student_id": new_student.id
    }