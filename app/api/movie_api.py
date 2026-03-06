from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.Entities.movie_model import Movie
from app.dtos.movie_create_dto import MovieCreateDTO
from app.dtos.movie_update_dto import  MovieUpdateDTO 

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


@router.put("/{movie_id}")
async def update_movie(movie_id: int, movie: MovieUpdateDTO, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    db_movie = result.scalar_one_or_none()

    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    if movie.name is not None:
        db_movie.name = movie.name

    if movie.actor_id is not None:
        db_movie.actor_id = movie.actor_id

    await db.commit()
    await db.refresh(db_movie)

    return db_movie