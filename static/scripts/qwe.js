
$(document).ready(function(){
    $(".delete-feedback").click(function(){
        var feedback_id = $("#id").val();
        $.ajax({
            url: '/view',
            method: 'DELETE',
            data: feedback_id,
            contentType: 'application/json;charset=UTF-8',
            success: function() {
                alert("Done");
                },
            error: function (xhr, textStatus, errorThrown) {
                console.log('Error in Operation');
             }
        });
    });
});
