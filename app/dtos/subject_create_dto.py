from pydantic import BaseModel

class SubjectCreateDTO(BaseModel):  
    code:str
    name:str 
    
    