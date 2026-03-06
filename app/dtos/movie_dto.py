from pydantic import BaseModel,ConfigDict
from typing import Optional

class MovieCreate(BaseModel):
    title:str
    year:Optional[int]=None
    actor_id:int
    
class MovieUpdate(BaseModel):
   title: Optional[str]=None
   year:Optional[int]=None
   actor_id:Optional[int]=None
class MovieResponse(BaseModel):
    id : int
    title: str
    year:Optional[int]=None
    actor_id:int
    
    class Config:
        from_attributes =True