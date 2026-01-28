from fastapi import FastAPI

from App.Core.database import engine
from App.Routers.auth import router as auth_router
from App.Routers.medicamento import router as medicamento_router

app = FastAPI(title="Consultorio Médico API")

app.include_router(auth_router)
app.include_router(medicamento_router)

# Test conexión DB
try:
    with engine.connect():
        print("Conexión exitosa a SQL")
except Exception as e:
    print("Error de conexión:", e)
