from pydantic import BaseModel

class MedicamentoCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    es_no_pos: bool = False

class MedicamentoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str | None
    es_no_pos: bool

    class Config:
        from_attributes = True
