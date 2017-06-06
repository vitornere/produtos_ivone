$(document).ready(function(){
    $('.carousel').carousel();
});

$('#login').webuiPopover({url:'#login-form'});

$(document).ready(function(){
    if($('#erro-login').is(":hidden")) {
        $('#login').click();
    }
});
