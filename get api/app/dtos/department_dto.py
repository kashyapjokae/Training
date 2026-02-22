from pydantic import BaseModel

class DepartmentCreateDTO(BaseModel):
    name: str

class DepartmentResponseDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True