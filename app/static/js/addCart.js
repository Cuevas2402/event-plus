$(document).ready(() =>{
    $('.add-btn').on('click', function(){
        
        const iid = $(this).val();

        $.ajax({
            url:'/add-cart',
            method: 'POST',
            data:{
                iid : iid,
            },
            success: function(response){
                location.reload();
            }
        });

    });

});
