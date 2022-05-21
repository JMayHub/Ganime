from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.url_map.strict_slashes = False #Añadiendo esto, no es necesaria la barra del final en la URL
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/ganime'

db = SQLAlchemy(app)

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

@app.route('/juego_anime/get/<int:id>', methods=['GET'])
def getJuego_animeById(id):
    #product = Product.query.get(id)
    juego_anime = Juego_anime.query.get_or_404(id)
    return juego_anime.toJSON()

@app.route('/juego_anime/put/<nombre>', methods=['GET'])
def putJuego_anime(nombre):
    juego_anime = Juego_anime(nombre)
    db.session.add(juego_anime)
    db.session.commit()
    return juego_anime.toJSON()

@app.route('/juego_anime/delete/<int:id>', methods=['GET'])
def deleteUsuarioById(id):
    juego_anime = Juego_anime.query.get(id)
    db.session.delete(juego_anime)
    db.session.commit()
    return juego_anime.toJSON()

@app.route('/juego_anime/all', methods=['GET'])
def allProducts():
    juegos_animes = Juego_anime.query.all()
    return jsonify(allJuegos_animes=[juego_anime.asdict() for juego_anime in juegos_animes])

if __name__ == '__main__':
    app.run( debug = True )