from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.registro_produccion import RegistroProduccion

from app.schemas.registro_produccion import (
    RegistroProduccionCreate
)

from app.schemas.registro_produccion import (
    RegistroProduccionResponse
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/registros-produccion")
def crear_registro_produccion(
    registro: RegistroProduccionCreate,
    db: Session = Depends(get_db)
):

    nuevo_registro = RegistroProduccion(

        empleado_id=registro.empleado_id,

        proceso_id=registro.proceso_id,

        op_id=registro.op_id,

        hora_inicio=registro.hora_inicio,

        hora_fin=registro.hora_fin
    )

    db.add(nuevo_registro)

    db.commit()

    db.refresh(nuevo_registro)

    return nuevo_registro

@router.get(
    "/registros-produccion",
    response_model=list[RegistroProduccionResponse]
)
def obtener_registros_produccion(
    db: Session = Depends(get_db)
):

    registros = db.query(
        RegistroProduccion
    ).all()

    return registros