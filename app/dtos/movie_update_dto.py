from pydantic import BaseModel

class MovieUpdateDTO(BaseModel):
    name: str