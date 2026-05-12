from pydantic import BaseModel


class EmpleadoCreate(BaseModel):
    nombre: str
    
class EmpleadoResponse(BaseModel):

    id: int

    nombre: str

    activo: bool

    class Config:

        from_attributes = True