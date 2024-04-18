jQuery(document).on("ready", function ($) {
    "use strict"
    $('[data-toggle="tooltip"]').tooltip();
    var wow = new WOW({
        boxClass: 'wow', // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset: 0, // distance to the element when triggering the animation (default is 0)
        mobile: true, // trigger animations on mobile devices (default is true)
        live: true, // act on asynchronously loaded content (default is true)
        callback: function (box) {
            // the callback is fired every time an animation is started
            // the argument that is passed in is the DOM node being animated
        },
        scrollContainer: null, // optional scroll container selector, otherwise use window,
        resetAnimation: true, // reset animation on end (default is true)
    });
    wow.init();
    /*---Header text slider, About image slider, About testimonial slider > Active ---*/
    $(".about-image-slide, .about-testimonial").owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        autoplayTimeout: 7000,
        smartSpeed: 500,
        center: true,
        nav: true,
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right" ></i>']
    });
    $(".header-text-carousel").owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        autoplayTimeout: 7000,
        smartSpeed: 500,
        center: true,
        nav: true,
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right" ></i>']
    });
    /*--- Testimonial slider Active---*/
    $(" .testimonial-items").owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        autoplayTimeout: 7000,
        smartSpeed: 500,
        center: true,
    });
    /*--- Client Slider Active ---*/
    $(".client-slide").owlCarousel({
        items: 6,
        loop: true,
        autoplay: true,
        autoplayTimeout: 7000,
        smartSpeed: 500,
        responsive: {
            // breakpoint from 0 up
            0: {
                items: 2,
            },
            // breakpoint from 480 up
            480: {
                items: 3,
            },
            // breakpoint from 768 up
            768: {
                items: 6,
            }
        }
    });
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    /*--- Circle Progress Bar Active ---*/
    $('.skill').percentcircle({
        animate: true,
        diameter: 100,
        guage: 10,
        coverBg: '#fff',
        bgColor: '#efefef',
        fillColor: '#D870A9',
        percentSize: '18px',
        percentWeight: 'normal'
    });

    $(' .single-gallery').each(function () {
        $(this).hoverdir();
    });

    // Initialize the gallery
    $('.gallery-icon a').touchTouch();
}(jQuery));