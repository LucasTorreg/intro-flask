# Aplicación de introducción a Flask

Programa hecho en python con el framework flask, Hello word

# Instalación 
- crear un entorno en python y ejecutar el comando:
```
pip install -r requirements.txt
```

la librería utilizada en flask https://flask-wtf.readthedocs.io/en/1.2.x/

# Ejecución del programa
-inicializar parámetros para servidor flask
-en mac:
```
export FLASK_APP=main.py
```
-en windows:
```
set FLASK_APP=main.py
```
-comando para ejecutar el servidor
```
flask --app main run
```
-comando para ejecutar el servidor en otro puerto diferente, por default es siempre el 5000
```
flask --app main run -p 5002
```
-comando para ejecutar el servidor en modo debug para realizar cambios en tiempo real
```
flask --app main --debug run
```