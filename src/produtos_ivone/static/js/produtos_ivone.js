$('.modal').modal();
$('#login').webuiPopover({url:'#login-form'});
$('#revista').modal('open')

// $("#test p").delay(1000).animate({ opacity: 1 }, 700);​

$(document).ready(function(){
    if($('#erro-login').is(":hidden")) {
        $('#login').click();
    }
	
});

$(document).ready(function(){
	var carousel_interval = 8000;
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