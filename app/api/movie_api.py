from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.entities.movie_model import Movie
from app.dtos.movie_dto import MovieCreate, MovieUpdate

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(title=movie.title, actor_id=movie.actor_id)

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


@router.get("/")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@router.put("/{movie_id}")
def update_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):

    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()

    db_movie.title = movie.title

    db.commit()

    return db_movie