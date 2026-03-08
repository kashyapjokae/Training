from pydantic import BaseModel,ConfigDict
from typing import Optional,List

class ActorCreate(BaseModel):
    name:str
   
class ActorUpdate(BaseModel):
    name: Optional[str]  =None
   

class ActorResponse(BaseModel):
    id : int
    name:str

    
   
class AwardNestedResponse(BaseModel):
    id: int
    award_name: str

    model_config = ConfigDict(from_attributes=True)


class MovieNestedResponse(BaseModel):
    id: int
    title: str
    year: Optional[int] = None
    awards: List[AwardNestedResponse] = []

    model_config = ConfigDict(from_attributes=True)


class ActorNestedResponse(BaseModel):
    id: int
    name: str
    movies: List[MovieNestedResponse] = []

    model_config = ConfigDict(from_attributes=True)


    class config:
        from_attributes=True