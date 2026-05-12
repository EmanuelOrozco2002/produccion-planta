from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/empleados")
def obtener_empleados(
    db: Session = Depends(get_db)
):

    empleados = db.query(Empleado).all()

    return empleados


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