jQuery.event.add(window, 'load', init);
jQuery.event.add(window, 'resize', resize);

var loc;
var cc = 0;
var latlng;
var myOptions;
var map;
var sound;
var activationCode = '';
var frame = '';
var isMobile = '';
var isTablet = '';

//Checking for mobile browser
if (navigator.userAgent.match(/iPad/i) ||
navigator.userAgent.match(/webOS/i) ||
navigator.userAgent.match(/Android 3.1/i)) {
    isTablet = true;
}
//Checking for mobile browser
else if (navigator.userAgent.match(/Android/i) ||
navigator.userAgent.match(/iPhone/i) ||
navigator.userAgent.match(/iPod/i)) {
    isMobile = true;
}

function activationCodeInit(code, html){
    activationCode = code + '';
    frame = html;
}

function jingleAnimate(id, x, y){
    var time = 2000;
    for (var i = 4; i > 0; i--) {
        if (i % 2 == 0) {
            $(id).animate({
                top: y + i * 5,
                left: x + i * 5,
            }, time / (i * 10));
        }
        else {
            $(id).animate({
                top: y - i * 5,
                left: x - i * 5,
            }, time / (i * 10));
        }
    }
}

function resize(){
    var height = $(window).height();
    var width = $(window).width();
    if (width > height && $("#bg img").height() > height) {
        $("#bg img").width(width);
        $("#bg img").height('auto');
    }
    else {
        $("#bg img").width('auto');
        $("#bg img").height(height);
    }
}

function getCookie(){
	if (document.cookie.match('foobar')) {
		return true;
	}
	else {
		document.cookie = 'foobar';
		return false;
	}
}

function init(){
    if (isTablet) {
		var width = $(window).width();
	    var height = $(window).height();
		if((width > height && width < 1000) || (height > width) && height < 1000){
			isTablet = false;
			isMobile = true;
		}
		else
            $('body').add($('div')).addClass('tablet');
    }
    if (isMobile) {
        $('body').add($('div')).addClass('mobile');
    }
    resize();
    //Current page = loc
    loc = window.location + "";
    loc = loc.split('/');
    loc = loc[loc.length - 1];
    $('#other-sounds > div').bind('click', function(){
        var incoming = $(this).next('div').clone();
        $(incoming).children('p').remove();
        //console.log(incoming);
        $('#current').remove();
        $(incoming).attr('id', 'current');
        $('#main').prepend(incoming);
    });
	$('#close-welcome').bind('click',function(){
		$('#welcome-popup').animate({
			opacity: 0,
		}, 300);
		window.setTimeout("$('#welcome-popup').css('z-index','-2');", 300);
	});
	$('#header').bind('click',function(){
		if ($('#welcome-popup').css('opacity') < .8) {
			$('#welcome-popup').animate({
				opacity: 1,
			}, 300);
			window.setTimeout("$('#welcome-popup').css('z-index','10');", 300);
		}
		else{
			$('#close-welcome').trigger('click');
		}
    });
	$('#activation_code').animate({
		opacity: 1
	}, 300);
    $('#activation_code').focus(function(){
        if ($('#activation_code').val() == '###') {
            $('#activation_code').val('');
        }
        //console.log($('#activation_code').val());
        $(document).keypress(function(event){
            if (event.which) {
                var key = event.which - 48;
            }
            else {
                var key = event.keyCode - 48;
            }
            if ($('#activation_code').val().match(activationCode) || ($('#activation_code').val() + key).match(activationCode)) {
                $(document).unbind('keypress');
                $('div.activation').remove();
                var sound = document.getElementById('sound');
                sound.play();
            }
            else {
                $('#activation_code').addClass('wrong-code');
            }
        });
    });
	if(getCookie()){
        $('#close-welcome').trigger('click');
    }
    if (loc == 'map') {
        $(document).mouseup(function(event){
            if ($('#marker-feed-back').data('new')) {
                $('#marker-feed-back').data('new', false);
                //                console.log($('#marker-feed-back').data('lat'));
                $('#lat').val($('#marker-feed-back').data('lat'));
                $('#long').val($('#marker-feed-back').data('long'));
                jingleAnimate('#marker-feed-back', event.pageX + 40, event.pageY - 70);
            }
        });
    }
}
