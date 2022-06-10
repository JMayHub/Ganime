var id = sessionStorage.getItem('id'); //Id del usuario logado.
var src = ""; //html del ranking que se irá creando más adelante.
var posicion = 0; //posición de cada personaje en el ranking.

//Conexión a la API para extraer la información del usuario logado con el Id.
fetch('http://localhost:5000/usuario/get/' + id)
.then(response => response.json())
.then(data => {
    document.getElementById('userUsuarioInicio').innerHTML = data.user;
    document.getElementById('imageUsuarioInicio').src = 'C:\\Users\\joanm\\Documents\\CFGS 2º Curso (DAM)\\Proyecto Final (Ganime)\\Ganime\\image\\' + data.image;
});

//Conexión a la API para obtener todos los personajes ordenados por votos y generar el ranking.
fetch('http://localhost:5000/personaje/all')
.then(response => response.json())
.then(data => {
    for(let i of data["allPersonajes"]){
        posicion++;
        if (posicion==1){
            src = src + "<tr onclick=\"location.href='file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Personaje%20Ganime.html?id=" + i.id + "'\"><th scope=\"row\" class=\"align-middle\"><h4 class=\"text-center\" style=\"color: gold;\">" + posicion + "º</h4></th><td class=\"align-middle\"><center><img src='..\\image\\" + i.imagen + "' class=\"rounded-circle\" width=\"75px\" height=\"75px\"></center></td><td class=\"align-middle\"><h4 class=\"text-center\">" + i.nombre + "</h4></td></tr>";
        }

        else if (posicion==2){
            src = src + "<tr onclick=\"location.href='file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Personaje%20Ganime.html?id=" + i.id + "'\"><th scope=\"row\" class=\"align-middle\"><h4 class=\"text-center\" style=\"color: silver;\">" + posicion + "º</h4></th><td class=\"align-middle\"><center><img src='..\\image\\" + i.imagen + "' class=\"rounded-circle\" width=\"75px\" height=\"75px\"></center></td><td class=\"align-middle\"><h4 class=\"text-center\">" + i.nombre + "</h4></td></tr>";
        }

        else if (posicion==3){
            src = src + "<tr onclick=\"location.href='file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Personaje%20Ganime.html?id=" + i.id + "'\"><th scope=\"row\" class=\"align-middle\"><h4 class=\"text-center\" style=\"color: #CD7F32;\">" + posicion + "º</h4></th><td class=\"align-middle\"><center><img src='..\\image\\" + i.imagen + "' class=\"rounded-circle\" width=\"75px\" height=\"75px\"></center></td><td class=\"align-middle\"><h4 class=\"text-center\">" + i.nombre + "</h4></td></tr>";
        }

        else {
            src = src + "<tr onclick=\"location.href='file:///C:/Users/joanm/Documents/CFGS%202%C2%BA%20Curso%20(DAM)/Proyecto%20Final%20(Ganime)/Ganime/public/Personaje%20Ganime.html?id=" + i.id + "'\"><th scope=\"row\" class=\"align-middle\"><h4 class=\"text-center\">" + posicion + "º</h4></th><td class=\"align-middle\"><center><img src='..\\image\\" + i.imagen + "' class=\"rounded-circle\" width=\"75px\" height=\"75px\"></center></td><td class=\"align-middle\"><h4 class=\"text-center\">" + i.nombre + "</h4></td></tr>";
        }
    }

    document.getElementById('tabla').innerHTML = src;
});