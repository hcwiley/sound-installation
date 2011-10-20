jQuery.event.add(window, 'load', init);

var loc;
var cc = 0;
var latlng;
var myOptions;
var map;
var sound;
var activationCode = '';
var frame = '';
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

function init(){
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
    $('#activation_code').focus(function(){
		//console.log($('#activation_code').val());
        $(document).keypress(function(event){
            if ($('#activation_code').val().match(activationCode)) {
				$(document).unbind('keypress');
				$('div.activation').remove();
				var div = document.createElement('DIV');
				$(div).html(frame);
                $('#current').append(div);
            }
        });
    });
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
