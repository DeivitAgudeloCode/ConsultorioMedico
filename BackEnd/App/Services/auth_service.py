from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from App.Core.database import SessionLocal
from App.Models.usuario import Usuario
from App.utils.password import hash_password, verify_password
from App.Core.security import create_access_token

def register_user(nombre: str, correo: str, password: str) -> Usuario:
    db: Session = SessionLocal()
    try:
        if db.query(Usuario).filter(Usuario.correo == correo).first():
            raise ValueError("El correo ya está registrado")

        user = Usuario(
            nombre=nombre,
            correo=correo,
            contraseña=hash_password(password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        raise ValueError("Error al crear el usuario")
    finally:
        db.close()

def login_user(correo: str, password: str) -> str:
    db: Session = SessionLocal()
    try:
        user = db.query(Usuario).filter(Usuario.correo == correo).first()
        if not user or not verify_password(password, user.contraseña):
            raise ValueError("Credenciales inválidas")

        return create_access_token({"sub": str(user.id)})
    finally:
        db.close()
