from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from App.Core.database import Base

class soliMedicamentos(Base):
    __tablename__ = "soliMedicamentos"

    id = Column(Integer, primary_key=True, index=True)



    numero_orden = Column(String, nullable=False)
    direccion = Column(String(150), nullable=False)
    telefono = Column(Integer, nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    fecha_creacion = Column(DateTime, server_default=func.now())