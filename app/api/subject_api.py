from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 
from app.core.database import get_db
from app.dtos.subject_create_dto import SubjectCreateDTO
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
        