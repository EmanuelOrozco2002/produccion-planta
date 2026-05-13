from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database import Base
from sqlalchemy.orm import relationship


class RegistroProduccion(Base):
    __tablename__ = "registros_produccion"

    id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=False)
    proceso_id = Column(Integer, ForeignKey("procesos.id"), nullable=False)
    op_id = Column(Integer, ForeignKey("ordenes_produccion.id"), nullable=False)
    hora_inicio = Column(DateTime, nullable=False)
    hora_fin = Column(DateTime, nullable=False)

    empleado = relationship("Empleado", back_populates="registros_produccion")
