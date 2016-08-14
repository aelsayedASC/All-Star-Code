var database = firebase.database().ref();
function sendMessage(){
    var name = $('#name').val();
    var message = $('#message').val();
    //Sending messages
    database.push({
        'name':name,
        'message':message
    });
    
}
$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
          
      }
    }
  });
});
(function($) {          
    $(document).ready(function(){                    
        $(window).scroll(function(){                          
            if ($(this).scrollTop() > 620) {
                $('#nav').fadeIn(500);
            } else {
                $('#nav').fadeOut(500);
            }
        });
    });
})(jQuery);

