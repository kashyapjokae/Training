from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.dtos.state_create_dto import state_request
router = APIRouter(prefix="/states", tags=["State Master"])

@router.post("/Create-State")
async def create_state(
    state: state_request,
    db: AsyncSession = Depends(get_db)
):
    return "hello i am working"


 