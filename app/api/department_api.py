from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dtos.department_dto import department_dto

router = APIRouter(prefix="/Department", tags=["Department Master"])


@router.post("/Create")
async def create_department(
    state: department_dto,
    db: Session = Depends(get_db)
):
    
    return {
        "message": "State created successfully"
    }