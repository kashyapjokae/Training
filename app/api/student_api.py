import shutil
from fastapi import APIRouter, Depends, UploadFile, File, Form , HTTPException 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


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


# LIST ALL STUDENTS
@router.get("/students")
async def get_students(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Student))
    students = result.scalars().all()

    return students 

# GET STUDENT BY ID
@router.get("/student/{student_id}")
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

# UPDATE STUDENT
@router.put("/update-student/{student_id}")
async def update_student(
    student_id: int,
    first_name: str = Form(...),
    last_name: str = Form(...),
    roll_no: int = Form(...),
    image: UploadFile = File(None),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if image:
        file_location = f"uploads/{image.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        student.image_path = file_location

    student.first_name = first_name
    student.last_name = last_name
    student.roll_no = roll_no

    await db.commit()
    await db.refresh(student)

    return student

# DELETE STUDENT
@router.delete("/delete-student/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    await db.delete(student)
    await db.commit()

    return {"message": "Student deleted successfully"} 