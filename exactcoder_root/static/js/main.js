'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut("slow");
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            FIlter
        --------------------*/
        $('.filter__controls li').on('click', function () {
            $('.filter__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.filter__gallery').length > 0) {
            var containerEl = document.querySelector('.filter__gallery');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    // Search model
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
		Hero Slider
	--------------------*/
    var hero_s = $(".hero__slider");
    hero_s.owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        nav: true,
        navText: ["<span class='arrow_carrot-left'></span>", "<span class='arrow_carrot-right'></span>"],
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 2000,
        autoHeight: false,
        autoplay: true,
        mouseDrag: false
    });

    /*------------------
        Video Player
    --------------------*/
    const player = new Plyr('#player', {
        controls: ['play-large', 'play', 'progress', 'current-time', 'mute', 'captions', 'settings', 'fullscreen'],
        seekTime: 25
    });

    /*------------------
        Niceselect
    --------------------*/
    $('select').niceSelect();

    /*------------------
        Scroll To Top
    --------------------*/
    $("#scrollToTopButton").click(function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
     });

     
    $(function(){
        /************** Normal Breadcrumb vedio background *********/

        function setVideoSize() {
            const vidWidth = 1280;
            const vidHeight = 720;
            const maxVidHeight = 400;
            let windowWidth = window.innerWidth;
            let newVidWidth = windowWidth;
            let newVidHeight = windowWidth * vidHeight / vidWidth;
            let marginLeft = 0;
            let marginTop = 0;
        
            if (newVidHeight < maxVidHeight) {
                newVidHeight = maxVidHeight;
                newVidWidth = newVidHeight * vidWidth / vidHeight;
            }
        
            if(newVidWidth > windowWidth) {
                marginLeft = -((newVidWidth - windowWidth) / 2);
            }
        
            if(newVidHeight > maxVidHeight) {
                marginTop = -((newVidHeight - $('#tm-video-container').height()) / 2);
            }
        
            const tmVideo = $('#tm-video');
        
            tmVideo.css('width', newVidWidth);
            tmVideo.css('height', newVidHeight);
            tmVideo.css('margin-left', marginLeft);
            tmVideo.css('margin-top', marginTop);
        }

        setVideoSize();

        // Set video background size based on window size
        let timeout;
        window.onresize = function () {
            clearTimeout(timeout);
            timeout = setTimeout(setVideoSize, 100);
        };

        // Play/Pause button for video background      
        const btn = $("#tm-video-control-button");

        btn.on("click", function (e) {
            const video = document.getElementById("tm-video");
            $(this).removeClass();

            if (video.paused) {
                video.play();
                $(this).addClass("fas fa-pause");
            } else {
                video.pause();
                $(this).addClass("fas fa-play");
            }
        });
    });

        // Quote carousel
        $(".quote-carousel").owlCarousel({
            center: true,
            autoplay: true,
            smartSpeed: 1000,
            dots: true,
            loop: true,
            responsive: {
                0:{
                    items:1
                },
                576:{
                    items:1
                },
                768:{
                    items:2
                },
                992:{
                    items:3
                }
            }
        });
        // Profile carousel
        $(".profile-carousel").owlCarousel({
            center: false,
            autoplay: false,
            smartSpeed: 1000,
            dots: false,
            loop: false,
            responsive: {
                0:{
                    items:1
                },
                576:{
                    items:1
                },
                768:{
                    items:2
                },
                992:{
                    items:3
                }
            }
        });
        

})(jQuery);

