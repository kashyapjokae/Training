from pydantic import BaseModel

class DepartmentCreateDTO(BaseModel):
    name: str