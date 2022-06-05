var queryString = window.location.search;
var urlParams = new URLSearchParams(queryString);
var id = urlParams.get('id');
var id_usuario = sessionStorage.getItem('id');
var votos = 0;

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

    fetch('http://localhost:5000/voto/get/personaje/' + id)
    .then(response => response.json())
    .then(data => {
        var crear_voto = 0;

        for(let i of data["allVotos"]) {
            if (i.personaje_id == id && i.estado == 1) {
                votos = votos + 1;
            }

            if(i.personaje_id == id && i.usuario_id == id_usuario) {
                crear_voto = 1;

                if (i.estado == 1) {
                    document.getElementById('like').src = '..\\image\\Like.png';
                }

                else {
                    document.getElementById('like').src = '..\\image\\noLike.png';
                }
            }
        }

        if (crear_voto == 0){
            fetch('http://localhost:5000//voto/get/last')
           .then(response => response.json())
           .then(data => {
                fetch('http://localhost:5000/voto/put/' + (data.id+1) + '/' + 0 + '/' + id_usuario + '/' + id)
                .then(response => response.json());
            })
        }

        fetch('http://localhost:5000/personaje/post/' + id + '/' + votos)
        .then(response => response.json())
        .then(data => document.getElementById('votos').innerHTML = data.votos);
    })
});

function votar() {
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);
    var id = urlParams.get('id');
    var id_usuario = sessionStorage.getItem('id');

    fetch('http://localhost:5000/voto/get/' + id + '/' + id_usuario)
    .then(response => response.json())
    .then(data => {
        if (data.estado == 1) {
            fetch('http://localhost:5000/voto/post/' + data.id + '/' + 0)
            .then (response => {
                var votos = parseInt(document.getElementById('votos').textContent);
                document.getElementById('votos').innerHTML = (votos-1);
                document.getElementById('like').src = '..\\image\\noLike.png';
                fetch('http://localhost:5000/personaje/post/' + id + '/' + (votos-1))
                    .then(response => response.json());
            });
        }

        else {
            fetch('http://localhost:5000/voto/post/' + data.id + '/' + 1)
            .then (response => {
                var votos = parseInt(document.getElementById('votos').textContent);
                document.getElementById('votos').innerHTML = (votos+1);
                document.getElementById('like').src = '..\\image\\Like.png';
                fetch('http://localhost:5000/personaje/post/' + id + '/' + (votos+1))
                .then(response => response.json());
            });
        }
    })
}