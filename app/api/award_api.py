from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.Entities.award import Award
from app.Entities.movie import Movie
from app.dtos.award_dto import AwardCreate, AwardUpdate, AwardResponse

router = APIRouter(prefix="/awards", tags=["Awards"])


@router.post("/", response_model=AwardResponse)
async def create_award(award: AwardCreate, db: AsyncSession = Depends(get_db)):
    movie_result = await db.execute(select(Movie).where(Movie.id == award.movie_id))
    movie = movie_result.scalar_one_or_none()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    new_award = Award(
    award_name=award.award_name,
    movie_id=award.movie_id


    )

    db.add(new_award)
    await db.commit()
    await db.refresh(new_award)
    return new_award


@router.get("/", response_model=list[AwardResponse])
async def get_awards(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Award))
    awards = result.scalars().all()
    return awards


@router.get("/{award_id}", response_model=AwardResponse)
async def get_award(award_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Award).where(Award.id == award_id))
    award = result.scalar_one_or_none()

    if not award:
        raise HTTPException(status_code=404, detail="Award not found")

    return award


@router.patch("/{award_id}", response_model=AwardResponse)
async def update_award(award_id: int, award: AwardUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Award).where(Award.id == award_id))
    award_obj = result.scalar_one_or_none()

    if not award_obj:
        raise HTTPException(status_code=404, detail="Award not found")

    update_data = award.dict(exclude_unset=True)

    if "movie_id" in update_data:
        movie_result = await db.execute(select(Movie).where(Movie.id == update_data["movie_id"]))
        movie = movie_result.scalar_one_or_none()

        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

    for key, value in update_data.items():
        setattr(award_obj, key, value)

    await db.commit()
    await db.refresh(award_obj)
    return award_obj


@router.delete("/{award_id}")
async def delete_award(award_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Award).where(Award.id == award_id))
    award = result.scalar_one_or_none()

    if not award:
        raise HTTPException(status_code=404, detail="Award not found")

    await db.delete(award)
    await db.commit()
    return {"message": "Award deleted successfully"}