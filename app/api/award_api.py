from fastapi import APIRouter, Depends , HTTPException   
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 


from app.core.database import get_db
from app.Entities.award_model import Award
from app.dtos.award_create_dto import AwardCreateDTO
from app.dtos.award_update_dto import AwardUpdateDTO

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


@router.put("/{award_id}")
async def update_award(award_id: int, award: AwardUpdateDTO, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Award).where(Award.id == award_id))
    db_award = result.scalar_one_or_none()

    if db_award is None:
        raise HTTPException(status_code=404, detail="Award not found")

    if award.name is not None:
        db_award.name = award.name

    if award.year is not None:
        db_award.year = award.year

    if award.movie_id is not None:
        db_award.movie_id = award.movie_id

    await db.commit()
    await db.refresh(db_award)

    return db_award