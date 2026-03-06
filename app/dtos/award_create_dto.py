from pydantic import BaseModel

class AwardCreateDTO(BaseModel):
    name: str
    year: int
    movie_id: int 