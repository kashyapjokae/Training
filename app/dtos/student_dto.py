from pydantic import BaseModel

class StudentResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    roll_no: str
    image_path: str

    class Config:
        orm_mode = True