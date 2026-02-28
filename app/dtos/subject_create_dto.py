from pydantic import BaseModel

class subject_dto(BaseModel):  
    code:str
    name:str 
    
    