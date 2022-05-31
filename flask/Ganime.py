from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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

class Personaje(db.Model):
    #Solo hay que indicar el nombre de la columna si se llama distinto del nombre del atributo
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30))
    apellidos = db.Column(db.String(60))
    armas_habilidades = db.Column(db.String(500))
    historia = db.Column(db.String(1000))
    imagen = db.Column(db.String(100))
    usuario_id = db.Column(db.Integer)
    juego_anime_id = db.Column(db.Integer)

    def __init__(self, id, nombre, apellidos, armas_habilidades, historia, imagen, usuario_id, juego_anime_id):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.armas_habilidades = armas_habilidades
        self.historia = historia
        self.imagen = imagen
        self.usuario_id = usuario_id
        self.juego_anime_id = juego_anime_id

    def asdict(self):
        return {"id": self.id,
                "nombre" : self.nombre,
                "apellidos" : self.apellidos,
                "armas_habilidades" : self.armas_habilidades,
                "historia" : self.historia,
                "imagen" : self.imagen,
                "usuario_id" : self.usuario_id,
                "juego_anime_id" : self.juego_anime_id}

    def toJSON(self):
        return jsonify(self.asdict())

class Juego_anime(db.Model):
    #Solo hay que indicar el nombre de la columna si se llama distinto del nombre del atributo
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column('nombre_juego_anime', db.String(30))

    def __init__(self, nombre):
        self.nombre = nombre

    def asdict(self):
        return {"id": self.id,
                "nombre" : self.nombre}

    def toJSON(self):
        return jsonify(self.asdict())

@app.route('/usuario/get/<int:id>', methods=['GET'])
def getUsuarioById(id):
    usuario = Usuario.query.get_or_404(id)
    return usuario.toJSON()

@app.route('/usuario/get/<string:user>/<string:password>', methods=['GET'])
def getUsuarioByLogin(user, password):
    usuario = Usuario.query.filter_by(user=user, password=password).first_or_404()
    return usuario.toJSON()

@app.route('/usuario/get/last', methods=['GET'])
def getLastUsuario():
    usuario = Usuario.query.order_by(Usuario.id.desc()).first()
    return usuario.toJSON()

@app.route('/usuario/put/<int:id>/<string:user>/<string:password>/<string:email>/<string:description>/blob:null/C:/fakepath/<string:imagen>', methods=['GET'])
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

@app.route('/personaje/get/<int:id>', methods=['GET'])
def getPersonajeById(id):
    personaje = Personaje.query.get_or_404(id)
    return personaje.toJSON()

@app.route('/personaje/get/last', methods=['GET'])
def getLastPersonaje():
    personaje = Personaje.query.order_by(Personaje.id.desc()).first()
    return personaje.toJSON()

@app.route('/personaje/put/<int:id>/<string:nombre>/<string:apellidos>/<string:armas_habilidades>/<string:historia>/<string:imagen>/<usuario_id>/<juego_anime_id>', methods=['GET'])
def putPersonaje(id, nombre, apellidos, armas_habilidades, historia, imagen, usuario_id, juego_anime_id):
    personaje = Personaje(id, nombre, apellidos, armas_habilidades, historia, imagen, usuario_id, juego_anime_id)
    db.session.add(personaje)
    db.session.commit()
    return personaje.toJSON()

@app.route('/personaje/delete/<int:id>', methods=['GET'])
def deletePersonajeById(id):
    personaje = Personaje.query.get(id)
    db.session.delete(personaje)
    db.session.commit()
    return personaje.toJSON()

@app.route('/personaje/all', methods=['GET'])
def allPersonajes():
    personajes = Personaje.query.all()
    return jsonify(allPersonajes=[personaje.asdict() for personaje in personajes])

@app.route('/juego_anime/get/<int:id>', methods=['GET'])
def getJuego_animeById(id):
    juego_anime = Juego_anime.query.get_or_404(id)
    return juego_anime.toJSON()

@app.route('/juego_anime/get/<string:nombre>', methods=['GET'])
def getJuego_animeByNombre(nombre):
    juego_anime = Juego_anime.query.filter_by(nombre=nombre).first_or_404()
    return juego_anime.toJSON()

@app.route('/juego_anime/put/<nombre>', methods=['GET'])
def putJuego_anime(nombre):
    juego_anime = Juego_anime(nombre)
    db.session.add(juego_anime)
    db.session.commit()
    return juego_anime.toJSON()

@app.route('/juego_anime/delete/<int:id>', methods=['GET'])
def deleteJuego_animeById(id):
    juego_anime = Juego_anime.query.get(id)
    db.session.delete(juego_anime)
    db.session.commit()
    return juego_anime.toJSON()

@app.route('/juego_anime/all', methods=['GET'])
def allJuegos_animes():
    juegos_animes = Juego_anime.query.all()
    return jsonify(allJuegos_animes=[juego_anime.asdict() for juego_anime in juegos_animes])

if __name__ == '__main__':
    app.run( debug = True )