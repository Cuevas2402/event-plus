$(document).ready(function() {
    $('select, input').on('change', function() {
        var categoria = $('#calificacion').val();
        var precio = $('#precio').val();
        var calificacion = $('#calificacion').val();
        var ubicacion = $('#ubicacion').val();
        var fecha = $('#fecha').val();
        
        var data = {
                categoria: categoria,
                precio: precio,
                calificacion: calificacion,
                ubicacion: ubicacion,
                fecha: fecha
            }
        console.log(data)
        /*
        $.ajax({
            url: '/filter',
            type: 'POST', 
            data: {
                categoria: categoria,
                precio: precio,
                calificacion: calificacion,
                ubicacion: ubicacion,
                fecha: fecha
            },
            success: function(response) {
            },
            error: function() {
                console.log('Error en la solicitud AJAX');
            }
        });*/
    });
});
