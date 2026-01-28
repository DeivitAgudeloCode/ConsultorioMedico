# 🏥 Consultorio Médico – Backend (FastAPI)

Backend del sistema **Consultorio Médico**, desarrollado con **FastAPI**.  
Expone una API REST con documentación automática vía Swagger.

---

## 🚀 Tecnologías

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- Passlib
- Bcrypt

---

## 📁 Estructura del proyecto

```text
ConsultorioMedico/
│
├── backend/              # Código del backend (FastAPI)
│   └── app/
│       └── main.py
│
├── .venv/                # Entorno virtual (NO subir al repositorio)
├── requirements.txt
└── README.md

⚙️ Instalación, ejecución y mantenimiento

1️⃣ Crear entorno virtual
python -m venv .venv

2️⃣ Activar entorno virtual (Windows)
.\.venv\Scripts\activate
Para desactivarlo:

deactivate
3️⃣ Instalar dependencias
python -m pip install -r requirements.txt

4️⃣ Versiones estables recomendadas
Para evitar errores de autenticación con bcrypt:
pip install passlib==1.7.4 bcrypt==3.2.2

5️⃣ Ejecutar el servidor
Ubícate en la carpeta backend y ejecuta:
uvicorn app.main:app --reload

🌐 Accesos
API
👉 http://127.0.0.1:8000

Documentación Swagger
👉 http://127.0.0.1:8000/docs

🧹 Limpieza de caché (pycache)
Si el proyecto presenta comportamientos extraños o errores persistentes, puedes limpiar la caché de Python ejecutando en PowerShell:

Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
Esto elimina todos los directorios __pycache__ sin necesidad de hacerlo manualmente.
