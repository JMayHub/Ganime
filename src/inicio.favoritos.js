var id = sessionStorage.getItem('id'); //Id del usuario logado.
var src = ""; //html del ranking que se irá creando más adelante.

//Conexión a la API para extraer la información del usuario logado con el Id.
fetch('http://localhost:5000/usuario/get/' + id)
.then(response => response.json())
.then(data => {
    document.getElementById('userUsuarioInicio').innerHTML = data.user;
    document.getElementById('imageUsuarioInicio').src = 'C:\\Users\\joanm\\Documents\\CFGS 2º Curso (DAM)\\Proyecto Final (Ganime)\\Ganime\\image\\' + data.image;
});

//Conexión a la API para obtener todos los personajes del usuario logado.
fetch('http://localhost:5000/voto/all/' + id)
.then(response => response.json())
.then(data => {
    for(let i of data["allVotos"]){
        if (i.estado == 1){
            fetch('http://localhost:5000/personaje/get/' + i.personaje_id)
            .then(response => response.json())
            .then(data => {
                src = src + "<div class=\"col-auto card\" onclick=\"location.href='file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Personaje%20Ganime.html?id=" + data.id + "'\"><img class=\"rounded m-2\" width=\"264.3px\" height=\"400px\" src=\"../image/" + data.imagen + "\" id=\"ImagePersonaje\"><h4 class=\"m-2\">" + data.nombre + " " + data.apellidos + "</h4></div>"
                document.getElementById('boxPersonajes').innerHTML = src;
            });
        }
    }
});