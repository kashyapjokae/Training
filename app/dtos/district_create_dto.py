from pydantic import BaseModel

class district_dto(BaseModel):
    district_code:str
    district_name:str 