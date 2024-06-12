
window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var fadeInPosition = 300; 

    if (scrollPosition >= fadeInPosition) {
        document.querySelector('.introduction').classList.add('fade-in');
    } else {
        document.querySelector('.introduction').classList.remove('fade-in');
    }
});


