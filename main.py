#importar la librería de flask
from flask import Flask

#inicializar la variable app con flask
app =  Flask(__name__)

#inicializar parámetros para servidor flask
#en mac:
#export FLASK_APP=main.py
#en wundows:
#set FLASK_APP=main.py

#comando para ejecutar el servidor
#flask --app main run

#comando para ejecutar el servidor en otro puerto diferente, por default es siempre el 5000
#flask --app main run -p 5002

#comando para ejecutar el servidor en modo debug para realizar cambios en tiempo real
#flask --app main --debug run

@app.route("/hola")
def hola_mundo():
    return "Hola mundo flask, esto e flask"