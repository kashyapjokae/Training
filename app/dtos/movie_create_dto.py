from pydantic import BaseModel

class MovieCreateDTO(BaseModel):
    title: str
    year: int
    actor_id: int