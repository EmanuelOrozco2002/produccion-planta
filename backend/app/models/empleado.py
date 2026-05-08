from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    activo = Column(Boolean, default=True)
    