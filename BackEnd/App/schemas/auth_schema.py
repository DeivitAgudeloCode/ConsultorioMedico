from pydantic import BaseModel, EmailStr, field_validator

class RegisterRequest(BaseModel):
    nombre: str
    correo: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str):
        if len(value.encode("utf-8")) > 72:
            raise ValueError("La contraseña no puede superar 72 bytes")
        if len(value) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return value

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
