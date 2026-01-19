function listadoUsuarios() {
    $.ajax({
        url: '/pais/',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            console.log(response);
        }
    });
}

$(document).ready(function() {
    listadoUsuarios();
});


