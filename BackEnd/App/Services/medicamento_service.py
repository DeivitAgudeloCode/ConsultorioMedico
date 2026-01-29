from sqlalchemy.orm import Session

from App.Core.database import SessionLocal
from App.Models.medicamento import Medicamento

def crear_medicamento(
    nombre: str,
    es_no_pos: bool
) -> Medicamento:
    db: Session = SessionLocal()
    try:
        medicamento = Medicamento(
            nombre=nombre,
            es_no_pos=es_no_pos
        )
        db.add(medicamento)
        db.commit()
        db.refresh(medicamento)
        return medicamento
    finally:
        db.close()

def listar_medicamentos() -> list[Medicamento]:
    db: Session = SessionLocal()
    try:
        return db.query(Medicamento).all()
    finally:
        db.close()
