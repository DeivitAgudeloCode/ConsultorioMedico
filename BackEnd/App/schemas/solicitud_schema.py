from pydantic import BaseModel
from typing import Optional

class SolicitudCreate(BaseModel):
    usuario_id: int
    medicamento_id: int
    num_orden: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo_contacto: Optional[str] = None


class SolicitudResponse(BaseModel): 
    id: int
    usuario_id: int
    medicamento_id: int
    estado: str

class Config:
    from_attributes = True
