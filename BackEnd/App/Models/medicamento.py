from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from App.Core.database import Base

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(255), nullable=True)
    es_no_pos = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, server_default=func.now())
