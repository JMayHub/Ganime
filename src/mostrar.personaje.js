var queryString = window.location.search;
var urlParams = new URLSearchParams(queryString);
var id = urlParams.get('id');

fetch('http://localhost:5000/personaje/get/' + id)
.then(response => response.json())
.then(data => {
    document.getElementById('ImagePersonaje').src='C:\\Users\\joanm\\Documents\\CFGS 2º Curso (DAM)\\Proyecto Final (Ganime)\\Ganime\\image\\' + data.imagen;
    document.getElementById('nombrePersonaje').innerHTML= data.nombre + " " + data.apellidos;
    document.getElementById('armasHabilidadesPersonaje').innerHTML = data.armas_habilidades;
    document.getElementById('historiaPersonaje').innerHTML = data.historia;
    fetch('http://localhost:5000/juego_anime/get/' + data.juego_anime_id)
    .then(response => response.json())
    .then(data => document.getElementById('juegoAnimePersonaje').innerHTML = data.nombre);
});