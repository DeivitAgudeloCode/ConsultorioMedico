from sqlalchemy.orm import Session

from App.Core.database import SessionLocal
from App.Models.usuario import Usuario
from App.Models.solicitudesMedicamentos import soliMedicamentos
from App.Models.medicamento import Medicamento

def crear_solicitud(
    usuario_id: Usuario,
    medicamento_id: int,
    num_orden: str | None,
    direccion: str | None,
    telefono: str | None,
    correo_contacto: str | None
) -> soliMedicamentos: 
    db: Session = SessionLocal()

    try: 
        medicamento = (
            db.query(Medicamento)
            .filter(Medicamento.id == medicamento_id)
            .first()
        )
        if not medicamento:
            raise ValueError("el medicamentos no se encuentra en al base de datos.")
        
        if medicamento.es_no_pos:
            if not all([
                num_orden,
                direccion,
                telefono,
                correo_contacto
            ]):
                raise ValueError("el medicamento es NO POS, debe ingresar direccion, telefono y correo.")
            
        solicitud = solicitud(
            usuario_id = usuario_id,
            medicamento_id = medicamento_id,
            numero_orden = num_orden,
            direccion=direccion,
            telefono= telefono,
            correo_contacto=correo_contacto
        )

        db.add(solicitud)
        db.commit()
        db.refresh(solicitud)

        return solicitud
    
    finally:
        db.close