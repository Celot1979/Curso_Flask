from flask import Flask,render_template,url_for,request,redirect
import os
app = Flask(__name__)
# Vamos a crear una lista para figurar una BBDD, y como pasar esta lista
# rendereizado
#1º Crear lista 
empleados=["Ana","Maria","Sandra","Juan"]


"""@app.route('/')
def hola_mundo():
    # 2º Para poder psar la info de la lista debemos
    # hacerlo en forma de clave valor en el parámetro del render_template

    return render_template('index.html', numeros_empleados = len(empleados))"""
# Nueva URL ( con su decorador y función).
# Cuando se abre el navegador, se debe de poner una barra inclinada y la plabra quienes.
# Automáticamente se reflajará lo que contiene la función.
@app.route('/quienes')
def quienes():
    #return "Esta es la página de quienes somos"
    return render_template('conocenos.html')

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
    #return "Bienvenido {}".format(numerousuario)
    return render_template('usuarios/usuarios.html', num_usuario=numerousuario)

@app.route('/usuario/<int:id>/<string:nombreusuario>')
def datosUsuario(id, nombreusuario):
    #return "Estos son los datos del usuario. Id: {}. Nombre del usuario: {}".format(id, nombreusuario)
    return render_template('usuarios/datosusuarios.html',id = id,nombreusuario=nombreusuario)

#En caso de que no se pase por parámetro a la URL, como controlar el error de la
#@app.route('/post')
@app.route('/post/<int:npost>')
def post(npost=0):
    #return "Bienvenido a la web " + str( numerousuario)
    return "Bienvenido {}".format(npost)
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#-- VISTAS DE LOS ELEMENTOS DEL MENÚ ------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
"""Ahora vamos a implementar las vistas 
de los diferentes elementos del formulario"""
@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre=request.form["nombre"]
        email=request.form["email"]
        contra=request.form["contra"]
        #Prueba de que se está guardando realmente la info que nos llega del formulario
        print("Nombre: " + nombre + ", Email: " + email + ", Contra: " + contra)

        # En principio vamos a rederigir el contenido a la página de inicio del
        # Posteriormente, la redirigimos a una BBDD
        return redirect(url_for('inicio'))


        #Si no hay info ó algo ha salido mal, directamente nos
        # renderiza la página.
    return render_template('contacto.html')




if __name__ == '__main__':
    os.environ['FLASK_ENV'] = "development"
    app.run(debug=True)