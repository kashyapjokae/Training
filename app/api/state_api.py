from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.dtos.state_create_dto import post_man_dto
from app.Entities.state_model import mummy_master
router = APIRouter(prefix="/states", tags=["State Master"])

@router.post("/Create-State")
async def create_state(
    state: post_man_dto,
    db: AsyncSession = Depends(get_db)
):
    new_state = mummy_master(
        name=state.madhu,
        code=state.payal
    )

    db.add(new_state)
    await db.commit()
    await db.refresh(new_state)

    return {
        "message": "State created successfully"
         
    }
 