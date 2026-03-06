from pydantic import BaseModel
from typing import Optional

class AwardCreate(BaseModel):
    award_name:str
    movie_id:int
    
class AwardUpdate(BaseModel):
   award_name: Optional[str]=None
   movie_id:Optional[int]=None
class AwardResponse(BaseModel):
    id : int
    award_name:str
    movie_id:int
    
    class Config:
        from_attributes=True
