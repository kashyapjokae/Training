from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 
from app.core.database import get_db
from app.dtos.subject_create_dto import SubjectCreateDTO 
from app.dtos.subject_update_dto import SubjectUpdateDTO
from app.Entities.subject_model import Subject
router = APIRouter(prefix="/subject", tags=["Subject Master"])

@router.post("/Create-Subject")
async def create_subject(
    subject: SubjectCreateDTO,
    db: AsyncSession = Depends(get_db)
):
    new_subject = Subject(
        code= subject.code,
        name= subject.name,
    )

    db.add(new_subject)
    await db.commit()
    await db.refresh(new_subject)

    return {
        "message": "Subject created successfully"

    }  

@router.get("/Get-Subjects")
async def get_subjects(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Subject))
    subjects = result.scalars() .all()
    return subjects 
        
@router.put("/Update-Subject/{id}")
async def update_subject(
    id: int,
    subject_data: SubjectUpdateDTO,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Subject).where(Subject.id == id))
    subject = result.scalars().first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    subject.name = subject_data.name
    subject.code = subject_data.code

    await db.commit()
    await db.refresh(subject)

    return subject        

@router.delete("/Delete-Subject/{id}")
async def delete_subject(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Subject).where(Subject.id == id))
    subject = result.scalars().first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    await db.delete(subject)
    await db.commit()

    return {"message": "Subject deleted successfully"}