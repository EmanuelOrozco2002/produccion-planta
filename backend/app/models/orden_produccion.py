from sqlalchemy import Column, Integer, String

from app.database import Base


class OrdenProduccion(Base):

    __tablename__ = "ordenes_produccion"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    codigo = Column(
        String,
        nullable=False
    )