from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = False
app.url_map.strict_slashes = False #Añadiendo esto, no es necesaria la barra del final en la URL
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/ganime'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

class Usuario(db.Model):
    #Solo hay que indicar el nombre de la columna si se llama distinto del nombre del atributo
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(20))
    description = db.Column(db.String(250))
    imagen = db.Column(db.String(100))

    def __init__(self, id, user, password, email, description, imagen):
        self.id = id
        self.user = user
        self.password = password
        self.email = email
        self.description = description
        self.imagen = imagen

    def asdict(self):
        return {"id": self.id,
                "user" : self.user,
                "password" : self.password,
                "email" : self.email,
                "description" : self.description,
                "image" : self.imagen}

    def toJSON(self):
        return jsonify(self.asdict())

@app.route('/usuario/get/<int:id>', methods=['GET'])
def getUsuarioById(id):
    #product = Product.query.get(id)
    usuario = Usuario.query.get_or_404(id)
    return usuario.toJSON()

@app.route('/usuario/get/last', methods=['GET'])
def getLastUsuario():
    #product = Product.query.get(id)
    usuario = Usuario.query.order_by(Usuario.id.desc()).first()
    return usuario.toJSON()

@app.route('/usuario/put/<id>/<user>/<string:password>/<string:email>/<string:description>/blob:null/C:/fakepath/<string:imagen>', methods=['GET'])
def putUsuario(id, user, password, email, description, imagen):
    usuario = Usuario(id, user, password, email, description, imagen)
    db.session.add(usuario)
    db.session.commit()
    return usuario.toJSON()

@app.route('/usuario/delete/<int:id>', methods=['GET'])
def deleteUsuarioById(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario.toJSON()

@app.route('/usuario/all', methods=['GET'])
def allUsuarios():
    usuarios = Usuario.query.all()
    return jsonify(allUsuarios=[usuario.asdict() for usuario in usuarios])

if __name__ == '__main__':
    app.run( debug = True )