//Función para el botón Login que comprobará si el usuario introducido existe en la BD y su contraseña es correcta.
function login() {
    var user = document.getElementById('inputUserLogin').value;
    var password = document.getElementById('inputPasswordLogin').value;

    //Login OK
    if (user != "" || password != "") {
        fetch('http://localhost:5000/usuario/get/' + user + '/' + password).catch(document.getElementById('camposObligatoriosLogin').innerHTML = 'El usuario y/o contraseña introducidos son incorrectos')
        .then(response => response.json())
        .then(data => {
            sessionStorage.setItem('id', (data.id)); //Guarda el id del usuario obtenido en la consulta, en una variable que compartirán el resto de archivos javascript.
            location.href = "file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Inicio%20Ganime.html"; //Redireccionamiento a la página principal de usuario.
        });
    }

    //Login ERROR
    else {
        document.getElementById('camposObligatoriosLogin').innerHTML = 'Uno de los dos campos está vacío';
    }
}