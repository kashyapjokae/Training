from pydantic import BaseModel
from typing import List
from app.dtos.movie_dto import MovieResponse


class ActorResponse(BaseModel):
    id: int
    name: str
    movies: List[MovieResponse]

    class Config:
        from_attributes = True