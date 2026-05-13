from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate, EmpleadoUpdate
from app.deps import get_db

router = APIRouter()


@router.get("/empleados")
def obtener_empleados(db: Session = Depends(get_db)):

    empleados = db.query(Empleado).all()

    return empleados


@router.get("/empleados/{empleado_id}")
def obtener_empleado(empleado_id: int, db: Session = Depends(get_db)):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    return empleado


@router.post("/empleados")
def crear_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):

    nuevo_empleado = Empleado(nombre=empleado.nombre)

    db.add(nuevo_empleado)

    db.commit()

    db.refresh(nuevo_empleado)

    return nuevo_empleado


@router.delete("/empleados/{empleado_id}")
def eliminar_empleado(empleado_id: int, db: Session = Depends(get_db)):

    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    db.delete(empleado)
    db.commit()
    return {"message": "Empleado eliminado correctamente"}


@router.put("/empleados/{empleado_id}")
def actualizar_empleado(
    empleado_id: int, empleado_update: EmpleadoUpdate, db: Session = Depends(get_db)
):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    empleado.nombre = empleado_update.nombre
    empleado.activo = empleado_update.activo
    db.commit()
    db.refresh(empleado)
    return empleado
