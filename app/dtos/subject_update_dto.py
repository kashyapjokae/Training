from pydantic import BaseModel

class SubjectUpdateDTO(BaseModel):
    name: str
    code: str 