from linio import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30), unique=True, nullable=False)
    descripcion = db.Column(db.String(100), unique=False, nullable=False)

class Comercio(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(9), unique=False, nullable=False)
    distrito = db.Column(db.String(2), unique=False, nullable=False)
    direccion = db.Column(db.String(40), unique=False, nullable=False)

db.create_all()