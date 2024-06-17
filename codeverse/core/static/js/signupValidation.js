const sendButton = docuement.getElementById('sendForm')

function formValidation() {
const nombre = document.getElementById("nombre").value
const usuario = document.getElementById("usuario").value
const correo_electronico = document.getElementById("correo_electronico").value
const contrasena1 = document.getElementById("contrasena1").value
const contrasena2 = document.getElementById("contraena2").value
if ((nombre || usuario || correo_electronico || contrasena1 || contrasena2) == '' ) {
    console.log("Debes completar los campos")
    return false
}else{
    console.log("campos completados correctamente")
    return true
}

}

sendButton.addEventListener('click',formValidation);