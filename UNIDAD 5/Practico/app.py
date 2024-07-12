from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import datetime
import hashlib

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuario, Receta, Ingrediente


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/bienvenido')
def bienvenido():
    return render_template('bienvenido.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['email'] or not request.form['password']:
            return render_template('error.html', error="Por favor ingrese los datos requeridos")
        else:
            usuario_actual = Usuario.query.filter_by(correo=request.form['email']).first()
            if usuario_actual is None:
                return render_template('error.html', error="El correo no está registrado")
            else:
                result = hashlib.md5(bytes(request.form['password'], encoding='utf-8'))
                if result.hexdigest() == usuario_actual.clave:
                    #session["usuario"] = usuario_actual
                    #print(session)
                    return render_template('bienvenido.html')
                else:
                    return render_template('error.html', error="La contraseña no es válida")


@app.route('/compartirreceta', methods=['GET', 'POST'])
def compartirreceta():
    if request.method == 'POST' or request.method == 'GET':
        #if Usuario in session:
         #   print('está')
        return render_template('compartirreceta.html')


@app.route('/ingreso_receta', methods=['GET', 'POST'])
def ingreso_receta():
    if request.method == 'POST' or request.method == 'GET':
        if not request.form["nombre"] or not request.form["tiempo"] or not request.form["descripcion"] or not \
                request.form["cing"]:
            return render_template('error.html', error="Por favor ingrese los datos requeridos")
        else:
            usuario_actual = request.form["usuario_actual"]
            nueva_receta = Receta(nombre=request.form["nombre"], tiempo=request.form["tiempo"], fecha=datetime.now(), elaboracion=request.form["descripcion"], cantidadmegusta=0, usuarioid=usuario_actual.id)
            db.session.add(nueva_receta)
            db.session.commit()
            x = int(request.form["cing"])
            return render_template('ingresaringredientes.html', x=x, recetaid=nueva_receta.id)


@app.route('/ingresaringredientes', methods=['GET', 'POST'])
def ingresaringredientes():
    if request.method == 'POST' or request.method == 'GET':
        band = False
        x = (int(request.form["x"])) - 1
        c=0
        while not band:
            nuevo_ingrediente = Ingrediente(nombre=request.form[f"nombrei{c}"], cantidad=request.form[f"cantidadi{c}"], unidad=request.form[f"unidad{c}"], recetaid=request.form["recetaid"])
            db.session.add(nuevo_ingrediente)
            db.session.commit()
            if c < x:
                c += 1
            elif c == x:
                band = True
        return render_template('ingredientescargados.html')


@app.route('/consultarranking', methods=['GET', 'POST'])
def consultarranking():
    if request.method == 'POST' or request.method == 'GET':
        listarecetas = Receta.query.order_by(Receta.cantidadmegusta.desc()).limit(5)
        return render_template('ranking.html', ordenada=listarecetas)


@app.route('/consultarreceta', methods=['GET', 'POST'])
def consultarreceta():
    return render_template('pidetiempo.html')


@app.route('/recetasportiempo', methods=['GET', 'POST'])
def recetasportiempo():
    if request.method == 'POST' or request.method == 'GET':
        tiempo = request.form["tiemporeceta"]
        listatiempomenor = Receta.query.filter(Receta.tiempo < tiempo)
        return render_template("muestrarecetastiempo.html", lista=listatiempomenor)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
