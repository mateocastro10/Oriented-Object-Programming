from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, relationship

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    receta = relationship("Receta", back_populates="usuario")


class Receta(db.Model):
    __tablename__ = "receta"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tiempo = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime)
    elaboracion = db.Column(db.Text)
    cantidadmegusta = db.Column(db.Integer, nullable=False)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="receta")
    ingredientes = relationship("Ingrediente", back_populates="receta")


class Ingrediente(db.Model):
    __tablename__ = "ingrediente"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)
    recetaid = db.Column(db.Integer, db.ForeignKey('receta.id'))
    receta = relationship("Receta", back_populates="ingrediente")