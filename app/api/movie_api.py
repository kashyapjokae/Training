from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.Entities.movie import Movie
from app.Entities.actor import Actor
from app.dtos.movie_dto import MovieCreate, MovieUpdate, MovieResponse

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/", response_model=MovieResponse)
async def create_movie(movie: MovieCreate, db: AsyncSession = Depends(get_db)):
    actor_result = await db.execute(select(Actor).where(Actor.id == movie.actor_id))
    actor = actor_result.scalar_one_or_none()

    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")

    new_movie = Movie(
        title=movie.title,
        year=movie.year,
        actor_id=movie.actor_id
    )

    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)
    return {
        "id": new_movie.id,
        "title": new_movie.title,
        "year": new_movie.year,
        "actor_id": new_movie.actor_id
    }


@router.get("/", response_model=list[MovieResponse])
async def get_movies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie))
    movies = result.scalars().all()
    return movies


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    movie = result.scalar_one_or_none()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie


@router.patch("/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: int, movie: MovieUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    movie_obj = result.scalar_one_or_none()

    if not movie_obj:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = movie.dict(exclude_unset=True)

    if "actor_id" in update_data:
        actor_result = await db.execute(select(Actor).where(Actor.id == update_data["actor_id"]))
        actor = actor_result.scalar_one_or_none()

        if not actor:
            raise HTTPException(status_code=404, detail="Actor not found")

    for key, value in update_data.items():
        setattr(movie_obj, key, value)

    await db.commit()
    await db.refresh(movie_obj)
    return movie_obj


@router.delete("/{movie_id}")
async def delete_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    movie = result.scalar_one_or_none()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    await db.delete(movie)
    await db.commit()
    return {"message": "Movie deleted successfully"}