var id = sessionStorage.getItem('id');
var src = "";

fetch('http://localhost:5000/usuario/get/' + id)
.then(response => response.json())
.then(data => {
    document.getElementById('userUsuarioInicio').innerHTML = data.user;
    document.getElementById('imageUsuarioInicio').src = 'C:\\Users\\joanm\\Documents\\CFGS 2º Curso (DAM)\\Proyecto Final (Ganime)\\Ganime\\image\\' + data.image;
});

/*fetch('http://localhost:5000/personaje/all')
.then(response => response.json())
.then(data => {
    
});*/