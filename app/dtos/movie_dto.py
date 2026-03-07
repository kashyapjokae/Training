from pydantic import BaseModel
from typing import List
from app.dtos.award_dto import AwardResponse


class MovieCreate(BaseModel):
    title: str
    actor_id: int


class MovieUpdate(BaseModel):
    title: str


class MovieResponse(BaseModel):
    id: int
    title: str
    awards: List[AwardResponse]

    class Config:
        from_attributes = True