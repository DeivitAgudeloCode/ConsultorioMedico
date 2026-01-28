from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from App.Core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    fecha_creacion = Column(DateTime, server_default=func.now())