var slideIndex = 1;

$( document ).ready(function() {
    console.log( "ready!debut" );

    showSlides(slideIndex);


    console.log( "ready!fin" );
});

function showSlides(n) {
    console.log( "ready!showSlides" );
    var i;

    var slides = document.getElementsByClassName("mySlides");

    var dots = document.getElementsByClassName("dot");

    if (n > slides.length) {slideIndex = 1}

    if (n < 1) {slideIndex = slides.length}

    for (i = 0; i < slides.length; i++) {

        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {

        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}

// Next/previous controls
function plusSlides(n) {
    console.log( "ready!plusSlides" );
    showSlides(slideIndex += n);
}
// Thumbnail image controls
function currentSlide(n) {
    console.log( "ready!currentSlides" );
    showSlides(slideIndex = n);
}