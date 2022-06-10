var queryString = window.location.search; //URL completa de la página.
var urlParams = new URLSearchParams(queryString); //Parámentros de la URL.
var id = urlParams.get('id'); //Parámetro Id del personaje.
var id_usuario = sessionStorage.getItem('id'); //Id del Usuario logado.
var votos = 0; //Número de votos inicial.

//Consulta a la API para obtener la información del usuario mediante su Id.
fetch('http://localhost:5000/personaje/get/' + id)
.then(response => response.json())
.then(data => {
    document.getElementById('ImagePersonaje').src='..\\image\\' + data.imagen;
    document.getElementById('nombrePersonaje').innerHTML= data.nombre + " " + data.apellidos;
    document.getElementById('armasHabilidadesPersonaje').innerHTML = data.armas_habilidades;
    document.getElementById('historiaPersonaje').innerHTML = data.historia;
    fetch('http://localhost:5000/juego_anime/get/' + data.juego_anime_id) //Consulta a la API para obtener la información del juego o anime del personaje.
    .then(response => response.json())
    .then(data => document.getElementById('juegoAnimePersonaje').innerHTML = data.nombre);

    //Consulta para obtener el número de votos del personaje.
    fetch('http://localhost:5000/voto/get/personaje/' + id)
    .then(response => response.json())
    .then(data => {
        var crear_voto = 0;

        //Cuenta el número de votos del personaje y comprueba si hay un registro de voto por este personaje del usuario logado.
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

        //Si no hay ningún registro de voto entre este personaje y el usuario logado se crea uno como no votado por defecto.
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

//Función para el botón de like que suma o resta 1 voto al personaje.
function votar() {
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);
    var id = urlParams.get('id');
    var id_usuario = sessionStorage.getItem('id');

    //Obtiene el registro de voto entre el personaje y el usuario y comprueba si el voto va a realizar va ser positivo o negativo.
    fetch('http://localhost:5000/voto/get/' + id + '/' + id_usuario)
    .then(response => response.json())
    .then(data => {
        if (data.estado == 1) { //Voto Negativo.
            fetch('http://localhost:5000/voto/post/' + data.id + '/' + 0)
            .then (response => {
                var votos = parseInt(document.getElementById('votos').textContent);
                document.getElementById('votos').innerHTML = (votos-1);
                document.getElementById('like').src = '..\\image\\noLike.png';
                fetch('http://localhost:5000/personaje/post/' + id + '/' + (votos-1))
                    .then(response => response.json());
            });
        }

        //Voto positivo.
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