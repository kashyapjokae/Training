from pydantic import BaseModel

class StudentCreateDTO(BaseModel):
    first_name: str
    last_name: str
    roll_no: int
    image_path: str