from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    actor_id: int

class MovieUpdate(BaseModel):
    title: str