from pydantic import BaseModel

class AwardCreate(BaseModel):
    award_name: str
    movie_id: int

class AwardUpdate(BaseModel):
    award_name: str