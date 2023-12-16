#importar la librería de flask
from flask import Flask

#inicializar la variable app con flask
app =  Flask(__name__)


@app.route("/hola")
def hola_mundo():
    return "Hola mundo flask, esto e flask"

#ejercicio, crear una ruta que devuelva una lista de frutas, el path sería /frutas
@app.route("/frutas")
def lista_frutas():
    list_fruta = ["Platano", "Fresa", "Piña", "Melón", "Naranja"]
    return list_fruta


@app.route("/nombre/<name>")
def tunombre(name):
    return f"hola {name}, cómo estás?"

@app.route("/numero/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"

#ejercicio tarea, realizar una ruta, que dinámicamente pueda solicitar o realizar
#operaciones de suma, resta, multiplicación y división según los parámetros pasados en la ruta

@app.route("/operacion/<int:valor1>/<operador>/<int:valor2>")
def operacion(valor1, operador, valor2):
    if operador == "+" or operador == "suma":
        return f"La suma de {valor1} y {valor2} es {valor1+valor2}"
    elif operador == "-" or operador == "resta":
        return f"La resta de {valor1} y {valor2} es {valor1-valor2}"
    elif operador == "*" or operador == "multiplicacion":
        return f"La multiplicación de {valor1} y {valor2} es {valor1*valor2}"
    elif operador == ":" or operador == "division":
        return f"La división de {valor1} y {valor2} es {valor1//valor2}"