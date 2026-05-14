from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate, EmpleadoUpdate, EmpleadoResponse
from app.deps import get_db

router = APIRouter()


@router.get("/empleados")
def obtener_empleados(
    activo: bool | None = None,
    nombre: str | None = None,
    orden: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    db: Session = Depends(get_db),
):
    empleados = db.query(Empleado)
    if activo is not None:
        empleados = empleados.filter(Empleado.activo == activo)
    if nombre is not None:
        empleados = empleados.filter(Empleado.nombre.like(f"%{nombre}%"))
    if orden is not None:
        if orden == "nombre":
            empleados = empleados.order_by(Empleado.nombre)
        elif orden == "id":
            empleados = empleados.order_by(Empleado.id)
    if limit is not None:
        empleados = empleados.limit(limit)
    if offset is not None:
        empleados = empleados.offset(offset)
    empleados = empleados.all()

    return empleados


@router.get("/empleados/{empleado_id}", response_model=EmpleadoResponse)
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
