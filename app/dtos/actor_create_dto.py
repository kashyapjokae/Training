from pydantic import BaseModel

class ActorCreateDTO(BaseModel):
    name: str