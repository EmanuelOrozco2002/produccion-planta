from pydantic import BaseModel
from datetime import datetime
from app.schemas.empleado import EmpleadoResponse


class RegistroProduccionCreate(BaseModel):

    empleado_id: int

    proceso_id: int

    op_id: int

    hora_inicio: datetime

    hora_fin: datetime


class RegistroProduccionResponse(BaseModel):

    id: int

    hora_inicio: datetime

    hora_fin: datetime

    empleado: EmpleadoResponse

    class Config:

        from_attributes = True
