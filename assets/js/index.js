function validar() {
  let texto = document.getElementById("#").value;
  if (texto == "") {
    document.getElementById("#").className = "text-danger";
    document.getElementById("#").innerHTML = "Debe ingresar el nombre";
  } else {
    document.getElementById("#").className = "text-success";
    document.getElementById("#").innerHTML = "Nombre correcto";
  }
}

function validar() {
  let texto = document.getElementById("#").value;
  if (texto == "") {
    document.getElementById("#").className = "text-danger";
    document.getElementById("#").innerHTML = "Debe ingresar el nombre";
  } else {
    document.getElementById("#").className = "text-success";
    document.getElementById("#").innerHTML = "Nombre correcto";
  }
}

function limpiar() {
  document.getElementById("#").innerHTML = "";
  document.getElementById("#").className = "";
  document.getElementById("#").innerHTML = "";
  document.getElementById("#").value = "";
}

var Fn = {
  // Valida el rut con su cadena completa "XXXXXXXX-X"
  validaRut: function (rutCompleto) {
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto)) return false;
    var tmp = rutCompleto.split("-");
    var digv = tmp[1];
    var rut = tmp[0];
    if (digv == "K") digv = "k";
    return Fn.dv(rut) == digv;
  },
  dv: function (T) {
    var M = 0,
      S = 1;
    for (; T; T = Math.floor(T / 10)) S = (S + (T % 10) * (9 - (M++ % 6))) % 11;
    return S ? S - 1 : "k";
  },
};

/* Uso de la función
alert( Fn.validaRut('11111111-1') ? 'Valido' : 'inválido');*/

const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll("#formulario input"); // Selecciona todos los inputs del formulario

const expresiones = {
  usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
  nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
  password: /^.{4,12}$/,
  telefono: /^\d{9}$/, // 9 numeros.
  correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
};

const validarFormulario = () => {};

inputs.forEach((input) => {
  input.addEventListener("keyup", validarFormulario);
  input.addEventListener("blur", validarFormulario);
});

formulario.addEventListener("submit", (e) => {
  e.preventDefault();
});

let carouselWidth = $(".carousel-inner")[0].scrollWidth;
let carWidth = $(".carousel-item").width();

let scrollPosition = 0;
$(".carousel-control-next").on("click", function () {
  console.log("next");
  scrollPosition = scrollPosition + carWidth;
  $(".carousel-inner").animate({ scrollleft: scrollPosition }, 600);
});