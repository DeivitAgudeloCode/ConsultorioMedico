from fastapi import APIRouter, Depends, status

from App.schemas.medicamento_schema import (
    MedicamentoCreate,
    MedicamentoResponse
)
from App.Services.medicamento_service import (
    crear_medicamento,
    listar_medicamentos
)
from App.Core.security import get_current_user
from App.Models.usuario import Usuario

router = APIRouter(
    prefix="/medicamentos",
    tags=["Medicamentos"]
)

@router.post(
    "",
    response_model=MedicamentoResponse,
    status_code=status.HTTP_201_CREATED
)
def crear(
    data: MedicamentoCreate,
    _: Usuario = Depends(get_current_user)
):
    return crear_medicamento(
        nombre=data.nombre,
        es_no_pos=data.es_no_pos
    )

@router.get(
    "",
    response_model=list[MedicamentoResponse]
)
def listar(_: Usuario = Depends(get_current_user)):
    return listar_medicamentos()
