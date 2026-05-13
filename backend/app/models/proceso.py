from sqlalchemy import Column, Integer, String

from app.database import Base


class Proceso(Base):

    __tablename__ = "procesos"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, nullable=False)
