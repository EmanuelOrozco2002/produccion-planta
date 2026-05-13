from pydantic import BaseModel
from app.schemas.registro_produccion import RegistroProduccionResponse
from typing import List


class EmpleadoCreate(BaseModel):
    nombre: str


class EmpleadoResponse(BaseModel):
    id: int
    nombre: str
    activo: bool

    registros_produccion: List[RegistroProduccionResponse]

    class Config:
        from_attributes = True


class EmpleadoUpdate(BaseModel):
    nombre: str
    activo: bool


class EmpleadoSimple(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True
