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

class Producto(db.Model):
   id =  db.Column(db.Integer, primary_key = True)
   nombre = db.Column(db.String(30), unique=True, nullable=False)
   precio = db.Column(db.Numeric(10,2), nullable=False)
   descripcion = db.Column(db.String(300), unique=False, nullable=False)
   comercio_id = db.Column(db.Integer, db.ForeignKey('comercio.id'), nullable=False)
   comercio = db.relationship('Comercio', backref=db.backref('comercio'))
   categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
   comercio = db.relationship('Categoria', backref=db.backref('categoria'))


db.create_all()