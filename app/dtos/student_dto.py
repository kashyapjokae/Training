from pydantic import BaseModel,ConfigDict
from typing import Optional

class StudentCreate(BaseModel):
    name :str
    age :int
    course :str

class StudentUpdate(BaseModel):
      name:Optional[str]=None
      age:Optional[int]=None
      course:Optional[str]=None
    
    
class StudentResponse(BaseModel):
        id:int
        name: str
        age:int
        course:str
        model_config = ConfigDict(from_attributes = True)  
 
 


