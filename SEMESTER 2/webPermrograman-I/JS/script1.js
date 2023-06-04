let menuBtn = document.querySelector('.hamburger');
let mobileMenu = document.querySelector('.mobile-nav');

menuBtn.addEventListener('click', function () {
    menuBtn.classList.toggle('is-active');
    mobileMenu.classList.toggle('is-active');
});

let menuBtn2 = document.querySelector('.hamburger-2');
let optionMenu = document.querySelector('.items');

menuBtn2.addEventListener('click', function () {
    menuBtn2.classList.toggle('is-active');
    optionMenu.classList.toggle('is-active');
});