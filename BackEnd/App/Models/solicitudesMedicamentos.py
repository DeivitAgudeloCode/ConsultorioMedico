from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from App.Core.database import Base

class soliMedicamentos(Base):
    __tablename__ = "solicitudes_medicamentos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    
    numero_orden = Column(String, nullable=False)
    direccion = Column(String(150), nullable=False)
    telefono = Column(String(150), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    fecha_creacion = Column(DateTime, server_default=func.now())

    usuario = relationship("Usuario")
    medicamento = relationship("Medicamento")