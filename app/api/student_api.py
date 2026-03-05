import shutil
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.Entities.student_model import Student

router = APIRouter(prefix="/student", tags=["Student"])

@router.post("/create-student")
async def create_student(
    first_name: str = Form(...),
    last_name: str = Form(...),
    roll_no: int = Form(...),
    image: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):

    file_location = f"uploads/{image.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    new_student = Student(
        first_name=first_name,
        last_name=last_name,
        roll_no=roll_no,
        image_path=file_location
    )

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)

    return new_student