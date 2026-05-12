from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate
from app.deps import get_db

router = APIRouter()

@router.get("/empleados")
def obtener_empleados(
    db: Session = Depends(get_db)
):

    empleados = db.query(Empleado).all()

    return empleados

@router.get("/empleados/{empleado_id}")
def obtener_empleado(
    empleado_id: int,
    db: Session = Depends(get_db)
):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()

    return empleado

@router.post("/empleados")
def crear_empleado(
    empleado: EmpleadoCreate,
    db: Session = Depends(get_db)
):

    nuevo_empleado = Empleado(
        nombre=empleado.nombre
    )

    db.add(nuevo_empleado)

    db.commit()

    db.refresh(nuevo_empleado)

    return nuevo_empleado