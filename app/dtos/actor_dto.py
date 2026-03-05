from pydantic import BaseModel

class ActorCreate(BaseModel):
    name: str

class ActorUpdate(BaseModel):
    name: str