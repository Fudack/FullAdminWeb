var modal = document.getElementById("myModal");
var btn_open = document.getElementById("open-modal");
var btn_close = document.getElementById("close-modal");
// JavaScript para mostrar el formulario de carga masiva
var importForm = document.getElementById("import-form");
var openImportFormBtn = document.getElementById("open-import-form");
modal.style.display = "none";

btn_open.onclick = function() {
    modal.style.display = "block";
    btn_open.style.display = "none";
}

btn_close.onclick = function() {
    modal.style.display = "none";
    btn_open.style.display = "block";
}


openImportFormBtn.onclick = function() {
    if (importForm.style.display === "block") {
        importForm.style.display = "none";
    } else {    
        importForm.style.display = "block";
    }
}