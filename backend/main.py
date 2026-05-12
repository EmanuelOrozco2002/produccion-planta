from fastapi import FastAPI

from app.routes import empleados
from app.routes import registros_produccion

from app.models.proceso import Proceso
from app.models.orden_produccion import OrdenProduccion


app = FastAPI()


app.include_router(empleados.router)

app.include_router(
    registros_produccion.router
)


@app.get("/")
def root():

    return {
        "message": "Sistema Produccion Planta funcionando"
    }