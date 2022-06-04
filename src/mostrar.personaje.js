var queryString = window.location.search;
var urlParams = new URLSearchParams(queryString);
var id = urlParams.get('id');
var id_usuario = sessionStorage.getItem('id');
var votos = 0;

fetch('http://localhost:5000/voto/get/personaje/' + id)
.then(response => response.json())
.then(data => {
    for(let i of data["allVotos"]) {
        if (i.personaje_id == id && i.estado == 1) {
            votos = votos + 1;
        }

        if(i.personaje_id == id && i.usuario_id == id_usuario) {
            if (i.estado == 1) {
                document.getElementById('like').src = '..\\image\\Like.png';
            }

            else {
                document.getElementById('like').src = '..\\image\\noLike.png';
            }
        }
    }
    document.getElementById('votos').innerHTML = votos;
})

fetch('http://localhost:5000/personaje/get/' + id)
.then(response => response.json())
.then(data => {
    document.getElementById('ImagePersonaje').src='..\\image\\' + data.imagen;
    document.getElementById('nombrePersonaje').innerHTML= data.nombre + " " + data.apellidos;
    document.getElementById('armasHabilidadesPersonaje').innerHTML = data.armas_habilidades;
    document.getElementById('historiaPersonaje').innerHTML = data.historia;
    fetch('http://localhost:5000/juego_anime/get/' + data.juego_anime_id)
    .then(response => response.json())
    .then(data => document.getElementById('juegoAnimePersonaje').innerHTML = data.nombre);
});

function votar() {
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);
    var id = urlParams.get('id');
    var id_usuario = sessionStorage.getItem('id');

    fetch('http://localhost:5000/voto/get/personaje/' + id)
    .then(response => response.json())
    .then(data => {
        for(let i of data["allVotos"]) {
            if(i.personaje_id == id && i.usuario_id == id_usuario) {
                if (i.estado == 1) {
                    fetch('http://localhost:5000/voto/post/' + i.id + '/' + 0)
                    .then (response => {
                        var votos = parseInt(document.getElementById('votos').textContent);
                        document.getElementById('votos').innerHTML = (votos-1);
                        document.getElementById('like').src = '..\\image\\noLike.png';

                    });
                }

                else {
                    fetch('http://localhost:5000/voto/post/' + i.id + '/' + 1)
                    .then (response => {
                        var votos = parseInt(document.getElementById('votos').textContent);
                        document.getElementById('votos').innerHTML = (votos+1);
                        document.getElementById('like').src = '..\\image\\Like.png';
                    });
                }
            }
        }
    })
}