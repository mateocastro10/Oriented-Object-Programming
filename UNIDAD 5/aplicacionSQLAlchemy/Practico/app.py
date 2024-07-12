from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from operator import attrgetter
import hashlib

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuario, Receta, Ingrediente


# global uid

@app.route('/')
def inicio():
    return render_template('inicio.html')


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
                    # global uid
                    # uid = usuario_actual
                    return render_template('bienvenido.html', usuario=usuario_actual)
                else:
                    return render_template('error.html', error="La contraseña no es válida")


@app.route('/compartirreceta', methods=['GET', 'POST'])
def compartirreceta():
    return render_template('compartirreceta.html')


@app.route('/ingreso_receta', methods=['GET', 'POST'])
def ingreso_receta():
    if request.method == 'POST' or request.method == 'GET':
        if not request.form["nombre"] or not request.form["tiempo"] or not request.form["descripcion"] or not \
                request.form["cing"]:
            return render_template('error.html', error="Por favor ingrese los datos requeridos")
        else:
            nueva_receta = Receta(nombre=request.form["nombre"], tiempo=request.form["tiempo"], fecha=datetime.now(),
                                  elaboracion=request.form["descripcion"], cantidadmegusta=0)  # usuarioid=uid.id)
            db.session.add(nueva_receta)
            db.session.commit()
            lista = []
            x = request.form["cing"]
            for i in x:
                lista.append(Ingrediente)
                render_template('ingresaringredientes.html')


@app.route('/ingresaringredientes', methods=['GET', 'POST'])
def ingresaringredientes():
    if request.method == 'POST' or request.method == 'GET':
        nuevo_ingrediente = Ingrediente(nombre=request.form["nombrei"], cantidad=request.form["cantidadi"],
                                        unidad=request.form["unidad"])
        db.session.add(nuevo_ingrediente)
        db.session.commit()
        return ('Ingrediente cargado')


@app.route('/consultarranking', methods=['GET', 'POST'])
def consultarranking():
    if request.method == 'POST' or request.method == 'GET':
        listarecetas = Receta.query.all()
        x = db.session.query(Receta).count() - 1
        ordenada = sorted(listarecetas, key=attrgetter('cantidadmegusta'), reverse=True)
        for i in range(5, x):
            ordenada.pop(i)
            x -= 1
        return render_template('ranking.html', ordenada=ordenada)


@app.route('/consultarreceta', methods=['GET', 'POST'])
def consultarreceta():
    return render_template('pidetiempo.html')


@app.route('/recetasportiempo', methods=['GET', 'POST'])
def recetasportiempo():
    if request.method == 'POST' or request.method == 'GET':
        tiempo = request.form["tiemporeceta"]
        print (tiempo)
        listatiempomenor = Receta.query.filter(Receta.tiempo < tiempo)
        return render_template("muestrarecetastiempo.html", lista=listatiempomenor)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
