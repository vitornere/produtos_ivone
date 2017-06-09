$(document).ready(function(){
	var carousel_interval = 1000;
	$('.carousel').carousel();
	var int;
	function run(){
	    int = setInterval(function()
	    { 
        	$('.carousel').carousel('next');
	    }, carousel_interval);
	}
	function stop(){
	clearInterval(int);
	}
	$('.carousel').hover(stop, run);     
});

$('#login').webuiPopover({url:'#login-form'});
$(document).ready(function(){
    if($('#erro-login').is(":hidden")) {
        $('#login').click();
    }
});

$(document).ready(function(){
     $('.modal').modal();
});

 $('#revista').modal('open')