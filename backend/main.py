from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.models.empleado import Empleado

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Sistema Produccion Planta funcionando"}


@app.get("/empleados")
def obtener_empleados(db: Session = Depends(get_db)):

    empleados = db.query(Empleado).all()

    return empleados