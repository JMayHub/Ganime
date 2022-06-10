// Obtener referencia al input y a la imagen

var inputImagen = document.getElementById('InputImageRegistroPersonaje');
var Imagen = document.getElementById('ImageRegistroPersonaje');

// Escuchar cuando cambie
inputImagen.addEventListener("change", () => {
  // Los archivos seleccionados, pueden ser muchos o uno
  const archivos = inputImagen.files;
  // Si no hay archivos salimos de la función y quitamos la imagen
  if (!archivos || !archivos.length) {
    Imagen.src = "";
    return;
  }
  // Ahora tomamos el primer archivo, el cual vamos a previsualizar
  const primerArchivo = archivos[0];
  // Lo convertimos a un objeto de tipo objectURL
  const objectURL = URL.createObjectURL(primerArchivo);
  // Y a la fuente de la imagen le ponemos el objectURL
  Imagen.src = objectURL;
});

//Función para el botón Registrar que comprobará si el personaje que se va a registrar es apto o falta información por completar.
function addPersonaje() {
    var nombre = document.getElementById("inputNombreRegistrarPersonaje").value;
    var apellidos = document.getElementById("inputApellidoRegistrarPersonaje").value;
    var juego_anime = document.getElementById("inputJuegoAnimeRegistrarPersonaje").value;
    var armas_habilidades = document.getElementById("inputArmasHabilidadesRegistrarPersonaje").value
    var historia = document.getElementById("inputHistoriaRegistrarPersonaje").value;
    var imagen = document.getElementById('InputImageRegistroPersonaje').value;
    var id_usuario = sessionStorage.getItem('id'); //Id del usuario logado/creador.
    var id = 0; //Id incial que cambiará y se le asignará al personaje.

    //Consulta del último personaje a la API para obtener su id, sumarle 1 y agregarlo al nuevo personaje.
    fetch('http://localhost:5000/personaje/get/last')
      .then(response => response.json())
      .then(data => id = (data.id+1));

    if (apellidos == "") {
      apellidos = " ";
    }

    if (historia == "") {
      historia = "Historia no disponible";
    }

    if (armas_habilidades == "") {
      armas_habilidades = "Armas y Habilidades no disponibles";
    }

    if (imagen == "") {
      imagen = "123456789012noImage.jpg";
    }

    //Registro Personaje OK
    if(nombre != "") {
        fetch('http://localhost:5000/juego_anime/get/' + juego_anime) //Obtiene el juego o anime que se le asignará al personaje.
        .then(response => response.json())
        .then(data => {
          fetch('http://localhost:5000/personaje/put/' + id + '/' + nombre + '/' + apellidos + '/' + armas_habilidades + '/' + historia + '/' + imagen.substring(12) + '/' + 0 +  '/' + id_usuario + '/' + data.id)
          .then(response => {
            console.log(response);
            location.href = "file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Inicio%20Ganime.html"; //Redireccionamiento a la página de Inicio.
          })
        })
    }
  
    //Registro Personaje ERROR
    else {
        document.getElementById('camposObligatoriosRegistro').innerHTML = 'El campo Nombre no a sido indicado';
    }
}