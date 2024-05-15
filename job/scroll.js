window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var fadeInPosition = 200; 

    if (scrollPosition >= fadeInPosition) {
        document.querySelector('.word').classList.add('fade-in');
    } else {
        document.querySelector('.word').classList.remove('fade-in');
    }
});


window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var fadeInPosition = 900; 

    if (scrollPosition >= fadeInPosition) {
        document.querySelector('.select').classList.add('fade-in');
    } else {
        document.querySelector('.select').classList.remove('fade-in');
    }
});

window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var fadeInPosition = 1500; 

    if (scrollPosition >= fadeInPosition) {
        document.querySelector('.res').classList.add('fade-in');
    } else {
        document.querySelector('.res').classList.remove('fade-in');
    }
});
