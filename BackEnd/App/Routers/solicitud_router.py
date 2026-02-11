from fastapi import APIRouter, Depends, status, HTTPException

from App.Schemas.solicitud_schema import (
    SolicitudCreate,
    SolicitudResponse
)
from App.Services.solicitud_service import crear_solicitud
from App.Core.security import get_current_user
from App.Models.usuario import Usuario

router = APIRouter(
    prefix="/solicitudes",
    tags=["solicitudes"]
)

@router.post(
    "",
    response_model=SolicitudResponse,
    status_code=status.HTTP_201_CREATED
)

def crearSoli(
    data: SolicitudCreate,
    current_user: Usuario = Depends(get_current_user)
):
    try:
        return crear_solicitud(
            usuario=current_user,
            medicamento_id=data.medicamento_id,
            num_orden=data.num_orden,
            direccion=data.direccion,
            telefono=data.telefono,
            correo_contacto=data.correo_contacto
        )
    except ValueError as e:
        raise HTTPException(
            status_code = 400,
            detail= str(e)
        )