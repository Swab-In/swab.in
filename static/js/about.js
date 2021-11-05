const popup = document.querySelector(".popup-box");
$('.button1').click(function () {
    popupBox();
})

$('.btn').click(function () {
    popupBox();
})

$('.button2').click(function () {
    redirect();
})

function popupBox() {
    popup.classList.toggle("open");
}

function redirect() {
    window.location.replace("contact");
}