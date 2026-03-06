from pydantic import BaseModel
from typing import Optional

class ActorCreate(BaseModel):
    name:str
   
class ActorUpdate(BaseModel):
    name: Optional[str]  =None
   

class ActorResponse(BaseModel):
    id : int
    name:str

    
    class config:
        from_attributes=True
