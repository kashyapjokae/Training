from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.Entities.movie_model import Movie
from app.dtos.movie_create_dto import MovieCreateDTO

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/")
async def create_movie(movie: MovieCreateDTO, db: AsyncSession = Depends(get_db)):

    new_movie = Movie(
        title=movie.title,
        year=movie.year,
        actor_id=movie.actor_id
    )

    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)

    return new_movie