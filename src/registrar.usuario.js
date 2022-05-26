// Obtener referencia al input y a la imagen

var inputImagen = document.getElementById('inputImageRegistrarUsuario');
var Imagen = document.getElementById('ImageRegistrarUsuario');

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

function addUsuario() {
    var user = document.getElementById("inputUserRegistroUsuario").value;
    var password = document.getElementById("inputPasswordRegistroUsuario").value;
    var email = document.getElementById("inputEmailRegistroUsuario").value
    var description = document.getElementById("inputDescriptionRegistroUsuario").value;
    var image = document.getElementById('inputImageRegistrarUsuario').value;

    if(user != "" && password != "" && email != "") {
      fetch('http://localhost:5000/usuario/get/last')
      .then(response => response.json())
      .then(data => fetch('http://localhost:5000/usuario/put/' + (data.id+1) + '/' + user + '/' + password + '/' + email + '/' + description + '/blob:null/C:/fakepath/' + image.substring(12)))
        .then(response => {
          location.href = "file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Inicio%20Ganime.html";
        }
      );
    }

    else {
      document.getElementById('camposObligatoriosRegistro').innerHTML = 'Uno de los campos obligatorios está vacío, porfavor, revise los campos con (*)';
    }
}