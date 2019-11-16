from linio import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    telefono = db.Column(db.String(9), unique=False, nullable=False)
    distrito = db.Column(db.String(2), unique=False, nullable=False)
    direccion = db.Column(db.String(40), unique=False, nullable=False)
    tarjeta = db.Column(db.String(16), unique=False, nullable=False)
    def __repr__(self):
        return '<Usuario %r>' % self.username


db.create_all()