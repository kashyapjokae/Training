from pydantic import BaseModel

class AwardUpdateDTO(BaseModel):
    name: str