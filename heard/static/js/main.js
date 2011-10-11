jQuery.event.add(window, 'load', init);

var loc;

function jingleAnimate(id, x, y){
    var time = 2000;
	for (var i = 4; i > 0; i--){
		if (i % 2 == 0) {
			$(id).animate({
				top: y + i * 5,
				left: x + i * 5,
			}, time/(i*10));
		}
		else{
			$(id).animate({
                top: y - i * 5,
                left: x - i * 5,
            }, time/(i*10));
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
        console.log(incoming);
        $('#current').remove();
        $(incoming).attr('id', 'current');
        $('#main').prepend(incoming);
    });
    if (loc == 'map') {
        $(document).mouseup(function(event){
            if ($('#marker-feed-back').data('new')) {
                $('#marker-feed-back').data('new', false);
//                console.log($('#marker-feed-back').data('lat'));
                $('#marker-feed-back p:first').text($('#marker-feed-back').data('lat'));
                $('#marker-feed-back p:last').text($('#marker-feed-back').data('long'));
                jingleAnimate('#marker-feed-back', event.pageX + 40, event.pageY - 70);
            }
        });
    }
}
