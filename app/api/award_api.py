from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.Entities.award_model import Award
from app.dtos.award_create_dto import AwardCreateDTO

router = APIRouter(prefix="/awards", tags=["Awards"])


@router.post("/")
async def create_award(award: AwardCreateDTO, db: AsyncSession = Depends(get_db)):

    new_award = Award(
        name=award.name,
        year=award.year,
        movie_id=award.movie_id
    )

    db.add(new_award)
    await db.commit()
    await db.refresh(new_award)

    return new_award