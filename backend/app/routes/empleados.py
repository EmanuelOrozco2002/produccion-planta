from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate, EmpleadoUpdate, EmpleadoResponse
from app.deps import get_db

router = APIRouter()


# funcion reutilizable para obtener un empleado por identificador
def obtener_empleado_por_id(db: Session, empleado_id: int):

    # Buscar empleado en base de datos
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()

    # Validar que el empleado exista
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


@router.get("/empleados", response_model=list[EmpleadoResponse])
def obtener_empleados(
    activo: bool | None = None,
    nombre: str | None = None,
    orden: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    db: Session = Depends(get_db),
):

    # Query base de empleados
    empleados = db.query(Empleado)

    # Filtrar por estado activo/inactivo
    if activo is not None:
        empleados = empleados.filter(Empleado.activo == activo)

    # Buscar empleados por coincidencia parcial en nombre
    if nombre is not None:
        empleados = empleados.filter(Empleado.nombre.like(f"%{nombre}%"))

    # Aplicar ordenamiento dinamico
    if orden is not None:
        # Ordenar por nombre
        if orden == "nombre":
            empleados = empleados.order_by(Empleado.nombre)

        # Ordenar por id
        elif orden == "id":
            empleados = empleados.order_by(Empleado.id)
            # validar campos de ordenamiento permitidos
        else:
            raise HTTPException(status_code=400, detail="Orden no permitido")

    # Limitar cantidad de resultados
    if limit is not None:
        empleados = empleados.limit(limit)

    # Saltar cierta cantidad de registros
    if offset is not None:
        empleados = empleados.offset(offset)

    # Ejecutar query SQL
    empleados = empleados.all()

    return empleados


@router.get("/empleados/{empleado_id}", response_model=EmpleadoResponse)
def obtener_empleado(empleado_id: int, db: Session = Depends(get_db)):
    empleado = obtener_empleado_por_id(db, empleado_id)

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

    empleado = obtener_empleado_por_id(db, empleado_id)

    db.delete(empleado)
    db.commit()
    return {"message": "Empleado eliminado correctamente"}


@router.put("/empleados/{empleado_id}")
def actualizar_empleado(
    empleado_id: int, empleado_update: EmpleadoUpdate, db: Session = Depends(get_db)
):
    empleado = obtener_empleado_por_id(db, empleado_id)
    empleado.nombre = empleado_update.nombre
    empleado.activo = empleado_update.activo
    db.commit()
    db.refresh(empleado)
    return empleado
