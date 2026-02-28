from pydantic import BaseModel

class department_dto(BaseModel):
    code:str
    name:str 