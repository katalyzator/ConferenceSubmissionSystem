
$(document).ready(function () {
    
    $('#custom-file-upload').change(function(e) {
        var filename = e.target.files[0].name;
        console.log(filename);
        $('.filupp-file-name').html(filename);
    });

    var txt = $('.comment > p');
    $(txt).each(function (i, obj) {
        if($(obj).text().length > 280) {
            $(obj).text($(obj).text().substring(0,277)+'...')
        }
    });

    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if( target.length ) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top
            }, 1000);
        }
    });

    $(function() {
        //----- OPEN
        $('[data-popup-open]').on('click', function(e)  {
            var targeted_popup_class = jQuery(this).attr('data-popup-open');
            $('[data-popup="' + targeted_popup_class + '"]').fadeIn(350);

            e.preventDefault();
        });

        //----- CLOSE
        $('[data-popup-close]').on('click', function(e)  {

            e.preventDefault();
            var targeted_popup_class = jQuery(this).attr('data-popup-close');
            $('[data-popup="' + targeted_popup_class + '"]').fadeOut(350);


        });
    });

    

});