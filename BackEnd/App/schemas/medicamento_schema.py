from pydantic import BaseModel

class MedicamentoCreate(BaseModel):
    nombre: str
    es_no_pos: bool = False

class MedicamentoResponse(BaseModel):
    id: int
    nombre: str
    es_no_pos: bool

    class Config:
        from_attributes = True
