from pydantic import BaseModel


class EmpleadoCreate(BaseModel):
    nombre: str