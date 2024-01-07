
    // (1) Inputmask (Phone)
    $(document).ready(function() {
        $(".phone-mask").inputmask("(+999) 999999-99999", {"onincomplete": function() {
            $(".phone-mask").val("");
            swal("Opss!","Incomplete Phone. Please review !", "info");
            return false;
        }});
    });
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
            dots: false,
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

        // Password Validition Check
        $("#password2").on("input", function() {
            // Get the values entered in the password and confirm password fields
            let password = $("#password1").val();
            let confirmPassword = $("#password2").val();
            let messageElement = $("#passwordMatchMessage");
            let submitBtn = $("#submitBtn");

            if (password === confirmPassword) {
                messageElement.text('Passwords match!').css("color", "green");
                submitBtn.prop("disabled", false);
            } else {
                messageElement.text('Passwords do not match. Please try again.').css("color", "red");
                submitBtn.prop("disabled", true);
            }
        });

        //=== Dropify Start===//
        $('.dropify').dropify({
            messages: { 'default': 'Click to Upload or Drag n Drop', 'remove':  '<i class="flaticon-close-fill"></i>', 'replace': 'Upload or Drag n Drop' }
        });
        setTimeout(function(){ $('.list-group-item.list-group-item-action').last().removeClass('active'); }, 100);

        //=== Dropify End===//

})(jQuery);


//=== Navbar Active class Start===//

document.addEventListener("DOMContentLoaded", function() {
    // Restore active state from localStorage
    let activeItem = localStorage.getItem("activeItem");
    if (activeItem) {
      let item = document.getElementById(activeItem);
      if (item) {
        item.classList.add('active');
      }
    }
  });

  function activeNav(itemName) {
    // Remove the 'active' class from all items
    let items = document.querySelectorAll('#nav li');
    items.forEach(function(item) {
      item.classList.remove('active');
    });

    // Add the 'active' class to the clicked item
    let item = document.getElementById(itemName);
    if (item) {
      item.classList.add('active');
    }

    // Save active state to localStorage
    localStorage.setItem("activeItem", itemName);
  }

//=== Navbar Active class end===//


//=== Navbar Active class end===//

//=== Category Item checked class add ===//
// function toggleCheckboxClass(className,checkbox) {
//     let checkedItem = document.querySelector(`label.${className}`)

//     if (checkbox.checked) {
//         checkedItem.classList.add("category_item_checked"); // Add the class for the checked state
//     } else {
//         checkedItem.classList.remove("category_item_checked"); // Remove the class for the unchecked state
//     }
//   }


//=== Social Media Sharing Start===//

const link = encodeURI(window.location.href);
// const link = 'https://exactcoder.com/projects';
// const msg = encodeURIComponent('Checkout Our Website');
// const titlemsg = encodeURIComponent(document.querySelector('.tille-for-social-share').textContent);

const fb = document.querySelector('.facebook-link');
fb.href = `https://www.facebook.com/sharer/sharer.php?u=${link}`;

// https://twitter.com/intent/tweet?
// const twitter = document.querySelector('.twitter-link');
// twitter.href = `http://twitter.com/share?&url=${link}&text=${titlemsg}&hashtags=exactcoder,programming`;

const linkedIn = document.querySelector('.linkedin-link');
linkedIn.href = `https://www.linkedin.com/sharing/share-offsite/?url=${link}`;

// const reddit = document.querySelector('.reddit');
// reddit.href = `http://www.reddit.com/submit?url=${link}&title=${titlemsg}`;

// const whatsapp = document.querySelector('.whatsapp');
// whatsapp.href = `https://api.whatsapp.com/send?text=${titlemsg}: ${link}`;

// const telegram = document.querySelector('.telegram');
// telegram.href = `https://telegram.me/share/url?url=${link}&text=${titlemsg}`;

//=== Social Media Sharing End===//

