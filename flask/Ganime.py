from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#Configuración del programa.
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/ganime'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

#Sincronizar BD con el programa.
db = SQLAlchemy(app)

class Usuario(db.Model):
    #Solo hay que indicar el nombre de la columna si se llama distinto del nombre del atributo.
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
    votos = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer)
    juego_anime_id = db.Column(db.Integer)

    def __init__(self, id, nombre, apellidos, armas_habilidades, historia, imagen, votos, usuario_id, juego_anime_id):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.armas_habilidades = armas_habilidades
        self.historia = historia
        self.imagen = imagen
        self.votos = votos
        self.usuario_id = usuario_id
        self.juego_anime_id = juego_anime_id

    def asdict(self):
        return {"id": self.id,
                "nombre" : self.nombre,
                "apellidos" : self.apellidos,
                "armas_habilidades" : self.armas_habilidades,
                "historia" : self.historia,
                "imagen" : self.imagen,
                "votos" : self.votos,
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

class Voto(db.Model):
    #Solo hay que indicar el nombre de la columna si se llama distinto del nombre del atributo
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column('estado', db.Integer)
    usuario_id = db.Column('usuario_id', db.Integer)
    personje_id = db.Column('personaje_id', db.Integer)

    def __init__(self, id, estado, usuario_id, personaje_id):
        self.id = id
        self.estado = estado
        self.usuario_id = usuario_id
        self.personje_id = personaje_id

    def asdict(self):
        return {"id": self.id,
                "estado" : self.estado,
                "usuario_id": self.usuario_id,
                "personaje_id": self.personje_id}

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

@app.route('/personaje/put/<int:id>/<string:nombre>/<string:apellidos>/<string:armas_habilidades>/<string:historia>/<string:imagen>/<int:votos>/<usuario_id>/<juego_anime_id>', methods=['GET'])
def putPersonaje(id, nombre, apellidos, armas_habilidades, historia, imagen, votos, usuario_id, juego_anime_id):
    personaje = Personaje(id, nombre, apellidos, armas_habilidades, historia, imagen, votos, usuario_id, juego_anime_id)
    db.session.add(personaje)
    db.session.commit()
    return personaje.toJSON()

@app.route('/personaje/post/<int:id>/<int:votos>', methods=['GET'])
def postPersonajeById(id, votos):
    personaje = Personaje.query.get_or_404(id)
    personaje.votos = votos
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
    personajes = Personaje.query.order_by(Personaje.votos.desc()).all()
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

@app.route('/voto/get/<int:id>', methods=['GET'])
def getVotoById(id):
    voto = Voto.query.get_or_404(id)
    return voto.toJSON()

@app.route('/voto/get/<int:personaje_id>/<int:usuario_id>', methods=['GET'])
def getVotoByPersonajeUsuario(personaje_id, usuario_id):
    voto = Voto.query.filter_by(personje_id=personaje_id, usuario_id=usuario_id).first_or_404()
    return voto.toJSON()

@app.route('/voto/get/last', methods=['GET'])
def getLastVoto():
    voto = Voto.query.order_by(Voto.id.desc()).first()
    return voto.toJSON()

@app.route('/voto/get/personaje/<int:personaje_id>', methods=['GET'])
def getVotoByPersonaje(personaje_id):
    votos = Voto.query.filter_by(personje_id=personaje_id).all()
    return jsonify(allVotos=[voto.asdict() for voto in votos])

@app.route('/voto/post/<int:id>/<int:estado>', methods=['GET'])
def postVotoById(id, estado):
    voto = Voto.query.get_or_404(id)
    voto.estado = estado
    db.session.commit()
    return voto.toJSON()

@app.route('/voto/put/<int:id>/<int:estado>/<int:usuario_id>/<int:personaje_id>', methods=['GET'])
def putVoto(id, estado, usuario_id, personaje_id):
    voto = Voto(id, estado, usuario_id, personaje_id)
    db.session.add(voto)
    db.session.commit()
    return voto.toJSON()

@app.route('/voto/delete/<int:id>', methods=['GET'])
def deleteVotoById(id):
    voto = Voto.query.get(id)
    db.session.delete(voto)
    db.session.commit()
    return voto.toJSON()

@app.route('/voto/all', methods=['GET'])
def allVotos():
    votos = Voto.query.all()
    return jsonify(allVotos=[voto.asdict() for voto in votos])

if __name__ == '__main__':
    app.run( debug = True )