from pydantic import BaseModel
from typing import Optional

class StudentCreate(BaseModel):
    first_name: str
    last_name:str
    roll_no:int
    age: int
    course: str
    image_path:Optional[str]

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name:Optional[str] = None
    roll_no:Optional[int] = None
    age: Optional[int] = None
    course: Optional[str] = None
    image_path:Optional[str]=None



class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name:str
    roll_no:int
    age: int
    course: str
    image_path:Optional[str]

    class Config:
        from_attibutes = True

    

 


