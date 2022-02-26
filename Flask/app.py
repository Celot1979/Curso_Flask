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
# Nueva URL ( con su decorador y función).
# Cuando se abre el navegador, se debe de poner una barra inclinada y la plabra quienes.
# Automáticamente se reflajará lo que contiene la función.
@app.route('/quienes')
def quienes():
    return "Esta es la página de quienes somos"

"""En este caso vamos crear el decorador y función para pasarle un
parámetro.
Así podremos ver la lección sobre parámetros de las URLs"""
#Parámetros con tipo string
@app.route('/usuarios/<string:nombreusuario>')
def usuarios(nombreusuario):
    return "Bienvenido a la web " + nombreusuario

#Parámetros con tipo entero
@app.route('/usuario/<int:numerousuario>')
def usuario(numerousuario):
    #return "Bienvenido a la web " + str( numerousuario)
    return "Bienvenido {}".format(numerousuario)

    
if __name__ == '__main__':
    os.environ['FLASK_ENV'] = "development"
    app.run(debug=True)