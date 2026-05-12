from pydantic import BaseModel
from datetime import datetime


class RegistroProduccionCreate(BaseModel):

    empleado_id: int

    proceso_id: int

    op_id: int

    hora_inicio: datetime

    hora_fin: datetime