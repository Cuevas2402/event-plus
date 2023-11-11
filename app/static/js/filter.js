$(document).ready(function() {
    $('select, input').on('change', function() {
        event.preventDefault();
        var categoria = $('#categoria').val();
        var precio = $('#precio').val();
        var calificacion = $('#calificacion').val();
        var ubicacion = $('#ubicacion').val();
        var fecha = $('#fecha').val();
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
                console.log(response.htmls[0])
                $('#cont').html('');
            },
            error: function() {
                console.log('Error en la solicitud AJAX');
            }
        });
    });
});
