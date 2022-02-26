from flask import Flask,render_template,url_for
import os
app = Flask(__name__)
# Vamos a crear una lista para figurar una BBDD, y como pasar esta lista
# rendereizado
#1º Crear lista 
empleados=["Ana","Maria","Sandra","Juan"]


@app.route('/')
def hola_mundo():
    # 2º Para poder psar la info de la lista debemos
    # hacerlo en forma de clave valor en el parámetro del render_template

    return render_template('index.html', numeros_empleados = len(empleados))
@app.route('/quienes')
def quienes():
    return "Esta es la página de quienes somos"

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = "development"
    app.run(debug=True)