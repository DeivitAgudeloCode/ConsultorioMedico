# ConsultorioMedico
# python -m pip install -r requirements.txt
# .\.venv\Scripts\activate
# deactivate para apagar el server .venv

# .venv es donde se aloja el reporsitorio de fast api 
# usar la carpeta de backend
# http://127.0.0.1:8000/docs

# uvicorn App.main:app --reload

# versiones de passlib y bcrypt estables 
# pip install passlib==1.7.4 bcrypt==3.2.2


# el siquiente codigo permite la limpieza de cache dentro del codigo para evitar tener que borrarlo manualmente
# Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force