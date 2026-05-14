from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class RegistroProduccionCreate(BaseModel):

    empleado_id: int = Field(gt=0)

    proceso_id: int = Field(gt=0)

    op_id: int = Field(gt=0)

    hora_inicio: datetime

    hora_fin: datetime

    @model_validator(mode="after")
    def validar_horas(self):
        if self.hora_inicio >= self.hora_fin:
            raise ValueError("La hora de inicio debe ser mayor a la hora final")
        return self


class RegistroProduccionResponse(BaseModel):

    id: int

    hora_inicio: datetime

    hora_fin: datetime

    class Config:

        from_attributes = True
