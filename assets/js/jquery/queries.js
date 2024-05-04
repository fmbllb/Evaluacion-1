$.validator.setDefaults({
  submitHandler: function () {
    alert("Formulario enviado.");
  },
});

$(document).ready(function () {
  $("#registroForm").validate({
    rules: {
      registroNombreUsuario: {
        required: true,
        minlength: 3,
      },
      registroNombre: {
        required: true,
        minlength: 5,
      },
      registroApellido: {
        required: true,
        minlength: 3,
        maxlength: 15,
      },
      registroEmail: {
        required: true,
        email: true,
      },
      /*comments: {
        required: true,
      },*/
      registroPass: {
        required: true,
        minlength: 5,
        maxlength: 12,
      },
      registroRepetirPass: {
        required: true,
        minlength: 8,
        equalTo: "#registroPass",
      },
      registroDireccion: {
        required: true,
        minlength: 6,
        maxlength: 50,
      },
      registroNumeroDireccion: {
        required: true,
        number: true,
        minlength: 1,
        maxlength: 6,
      },
      registroRegion: "required",
      registroComuna: "required",
    },
    messages: {
      registroNombreUsuario: {
        required: "Por favor, ingresa tu nombre de usuario.",
        minlength: "Tu nombre de usuario debe ser de al menos 3 caracteres.",
      },
      registroNombre: {
        required: "Por favor, ingresa tu nombre completo.",
        minlength: "Tu nombre debe ser de al menos 5 caracteres.",
      },
      registroApellido: {
        required: "Por favor, ingresa tu apellido completo.",
        minlength: "Tu apellido debe ser de al menos 3 caracteres.",
        maxlength: "Tu apellido no debe exceder los 15 caracteres.",
      },
      registroEmail: "Por favor ingresa un correo válido.",
      /*comments: "Por favor ingresa un comentario",*/
      registroPass: {
        required: "Por favor, ingresa una contraseña.",
        minlength:
          "Tu contraseña debe ser de al menos 8 caracteres de longitud.",
        maxlength: "Tu contraseña no debe exceder los 16 caracteres.",
      },
      registroRepetirPass: {
        required: "Ingresa la contraseña de nuevo.",
        minlength:
          "Tu contraseña debe ser de al menos 8 caracteres de longitud.",
        equalTo: "Por favor, ingresa la misma contraseña de arriba.",
      },
      registroDireccion: {
        required: "Por favor, ingresa una dirección.",
        minlength: "Tu dirección debe ser de al menos 6 caracteres.",
        maxlength: "Tu dirección no debe exceder los 50 caracteres.",
      },
      registroNumeroDireccion: {
        required: "Por favor, ingresa un número de dirección.",
        number: "Por favor, ingresa un número válido.",
        minlength: "Tu número de dirección debe ser de al menos 1 dígito.",
        maxlength: "Tu número de dirección no debe exceder los 6 dígitos.",
      },
      registroRegion: "Por favor, indica una región.",
      registroComuna: "Por favor, indica una comuna.",
      luckynumber: {
        required: "Por favor",
      },
    },
    errorElement: "em",
    errorPlacement: function (error, element) {
      // Add the `help-block` class to the error element
      error.addClass("help-block");

      if (element.prop("type") === "checkbox") {
        error.insertAfter(element.parent("label"));
      } else {
        error.insertAfter(element);
      }
    },
    highlight: function (element, errorClass, validClass) {
      $(element)
        .parents(".col-sm-10")
        .addClass("has-error")
        .removeClass("has-success");
    },
    unhighlight: function (element, errorClass, validClass) {
      $(element)
        .parents(".col-sm-10")
        .addClass("has-success")
        .removeClass("has-error");
    },
  });
});
