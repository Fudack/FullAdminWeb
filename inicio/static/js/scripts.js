var modal = document.getElementById("myModal");
var btn_open = document.getElementById("open-modal");
var btn_close = document.getElementById("close-modal");
modal.style.display = "none";

btn_open.onclick = function() {
    modal.style.display = "block";
    btn_open.style.display = "none";
}

btn_close.onclick = function() {
    modal.style.display = "none";
    btn_open.style.display = "block";
}