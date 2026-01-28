from fastapi import APIRouter, HTTPException, status, Depends
from App.Schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse
from App.Services.auth_service import register_user, login_user
from App.Core.security import get_current_user
from App.Models.usuario import Usuario

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest):
    try:
        user = register_user(
            nombre=data.nombre,
            correo=data.correo,
            password=data.password
        )
        return {"id": user.id, "nombre": user.nombre, "correo": user.correo}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    try:
        token = login_user(correo=data.correo, password=data.password)
        return {"access_token": token}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )

@router.get("/me")
def me(current_user: Usuario = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "nombre": current_user.nombre,
        "correo": current_user.correo
    }
