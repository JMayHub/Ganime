from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.url_map.strict_slashes = False #Añadiendo esto, no es necesaria la barra del final en la URL
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/ganime'

db = SQLAlchemy(app)

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

    def __init__(self, nombre, apellidos, armas_habilidades, historia, imagen, usuario_id, juego_anime_id):
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

@app.route('/personaje/get/<int:id>', methods=['GET'])
def getPersonajeById(id):
    #product = Product.query.get(id)
    personaje = Personaje.query.get_or_404(id)
    return personaje.toJSON()

@app.route('/personaje/put/<nombre>/<string:apellidos>/<string:armas_habilidades>/<string:historia>/<string:imagen>/<usuario_id>/<juego_anime_id>', methods=['GET'])
def putPersonaje(nombre, apellidos, armas_habilidades, historia, imagen, usuario_id, juego_anime_id):
    personaje = Personaje(nombre, apellidos, armas_habilidades, historia, imagen, usuario_id, juego_anime_id)
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
def allProducts():
    personajes = Personaje.query.all()
    return jsonify(allPersonajes=[personaje.asdict() for personaje in personajes])

if __name__ == '__main__':
    app.run( debug = True )