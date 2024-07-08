$.validator.setDefaults({
  submitHandler: function () {
    console.log("Formulario enviado.");
  },
});

$(document).ready(function () {
  $("#registroForm").validate({
    rules: {
      registroNombreUsuario: {
        required: true,
        minlength: 3,
        expresionesReg: /^[a-zA-Z.\-_\/,]+$/,
      },
      registroNombre: {
        required: true,
        minlength: 3,
        expresionesReg: /^[a-zA-Z]+$/,
      },
      registroApellido: {
        required: true,
        minlength: 3,
        maxlength: 15,
        expresionesReg: /^[a-zA-Z]+$/,
      },
      registroEmail: {
        required: true,
        email: true,  
        expresionesReg: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/,
      },
      /*comments: {
        required: true,
      },*/
      registroPass: {
        required: true,
        minlength: 5,
        maxlength: 12,
        expresionesReg: /^(?=.*[$%&*()\-_=+!#])(?=.*[a-z])(?=.*[A-Z])\S+$/,
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
        expresionesReg: /^[a-zA-Z]+$/,
      },
      registroNumeroDireccion: {
        required: true,
        number: true,
        minlength: 1,
        maxlength: 6,
        expresionesReg: /^[0-9]+$/,
      },
      registroRegion: "required",
      registroComuna: "required",
    },
    messages: {
      registroNombreUsuario: {
        required: "Por favor, ingresa tu nombre de usuario.",
        minlength: "Tu nombre de usuario debe ser de al menos 3 caracteres.",
        expresionesReg:
          "Por favor, ingresa un nombre de usuario válido. (solo se aceptan letras y  '.', '-', '_', ',', '/'.)",
      },
      registroNombre: {
        required: "Por favor, ingresa tu nombre completo.",
        minlength: "Tu nombre debe ser de al menos 3 caracteres.",
        expresionesReg: "Por favor, ingresa un nombre válido. (solo letras)",
      },
      registroApellido: {
        required: "Por favor, ingresa tu apellido completo.",
        minlength: "Tu apellido debe ser de al menos 3 caracteres.",
        maxlength: "Tu apellido no debe exceder los 15 caracteres.",
        expresionesReg: "Por favor, ingresa un apellido válido. (solo letras)",
      },
      registroEmail: {
        required: "Por favor, ingresa tu correo electrónico.",
        email: "Por favor, ingresa un correo electrónico válido.",
        expresionesReg: "Por favor, ingresa un correo válido.",
      },
      /*comments: "Por favor ingresa un comentario",*/
      registroPass: {
        required: "Por favor, ingresa una contraseña.",
        minlength:
          "Tu contraseña debe ser de al menos 8 caracteres de longitud.",
        maxlength: "Tu contraseña no debe exceder los 16 caracteres.",
        expresionesReg:
          "Por favor, ingresa una contraseña con al menos una letra mayúscula, una letra minúscula, un número y un carácter especial y sin Espacios en blanco.",
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
        expresionesReg: "Por favor, ingresa una dirección válida.",
      },
      registroNumeroDireccion: {
        required: "Por favor, ingresa un número de dirección.",
        number: "Por favor, ingresa un número válido.",
        minlength: "Tu número de dirección debe ser de al menos 1 dígito.",
        maxlength: "Tu número de dirección no debe exceder los 6 dígitos.",
        expresionesReg: "Por favor, ingresa un número de dirección válido.",
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
      error.addClass("help-block").css("color", "red");

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
// Validando el registro de inicio de sesión
$(document).ready(function () {
  $("#registroInicio").validate({
    //Declarando las reglas explicitas de validacion
    rules: {
      //Valida que el correo este presente
      inicioCorreo: {
        required: true,
        email: true,
        minlength: 3,
        expresionesReg: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/,
      },
      //Valida que la contraseña este presente y con el formato correcto
      passInicio: { 
        required: true, 
        minlength: 8, 
        maxlength: 16,
        expresionesReg: /^(?=.*[$%&*()\-_=+!#])(?=.*[a-z])(?=.*[A-Z])\S+$/,
      },
    },
    messages: {
      //Envia mensajes de error si no se cumple con las reglas de validacion
      inicioCorreo: {
        required: "Por favor, ingresa tu nombre de usuario.",
        email: "Por favor, ingresa un correo electrónico válido.",
        minlength: "Tu nombre de usuario debe tener al menos 3 caracteres.",
        expresionesReg: "Por favor, ingresa un correo valido. (Solo se aceptan letras y caracteres especiales (No se acepta *)).",
      },
      passInicio: { 
        required: "Por favor, ingresa tu contraseña.", 
        minlength: "Tu contraseña debe tener al menos 8 caracteres.", 
        maxlength: "Tu contraseña no debe exceder los 16 caracteres.",
        expresionesReg: "Debes introducir una contraseña valida.",
      },
    },
    errorElement: "em",
    errorPlacement: function (error, element) {
      //Gestionar errores.
      error.addClass("help-block").css("color", "red");

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

//Validacion del rut.registroRut
$(document).ready(function () {
  $("#validacion-live").validate({
    //Declarando las reglas explicitas de validacion
    rules: {
      //Valida que el rut este presente
      registroRut: {
        required: true,
        minlength: 7,
        expresionesReg: /^[0-9]+[-|‐]{1}[0-9kK]{1}$/,
      },

    },
    messages: {
      //Envia mensajes de error si no se cumple con las reglas de validacion
      registroRut: {
        required: "Por favor, ingresa tu rut.",
        minlength: "Tu rut debe tener al menos 7 caracteres.",
        expresionesReg: "Por favor, ingresa un rut valido.",
      },
    },
    errorElement: "em",
    errorPlacement: function (error, element) {
      //Gestionar errores.
      error.addClass("help-block").css("color", "red");

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

$(document).ready(function () {
  // Definir la regla personalizada utilizando addMethod
  $.validator.addMethod(
    "expresionesReg",
    function (value, element, regex) {
      return this.optional(element) || regex.test(value);
    },
    "Por favor, introduce un valor válido."
  );
});


$(document).ready(function() {
  // Manejar el evento de clic en el botón de decremento
  $('#decrement').on('click', function() {
    adjustQuantity(-1);
  });

  // Manejar el evento de clic en el botón de incremento
  $('#increment').on('click', function() {
    adjustQuantity(1);
  });

  // Calcular el valor total al cambiar la cantidad
  $('#qtyInput').on('input', function() {
    calculateTotal();
  });
});

function calculateTotal() {
  const quantityInput = $('#qtyInput');
  const price = 6500; // Precio del producto
  const quantity = parseInt(quantityInput.val());
  const total = price * quantity;
  const impuestos = total * 0.38; // 38% de impuestos
  const totalConImpuestos = total + impuestos;

  $('#totalValue').text(`$${total}`);

    // Actualizar los valores en las secciones correspondientes
    $('#totalValue').text(`$${total}`);
    $('#ctdTotalProductos').text(`${quantity} artículo(s) - $ ${total}`);
    $('#totalConImpuestos').text(`Total (impuestos inc.) - $ ${totalConImpuestos.toFixed(2)}`);
}

function adjustQuantity(change) {
  const quantityInput = $('#qtyInput');
  const currentValue = parseInt(quantityInput.val());
  const newValue = currentValue + change;
  if (newValue >= 1 && newValue <= 10) {
    quantityInput.val(newValue);
    calculateTotal();
  }
}

$(document).ready(function() {
  $('#recuperarContrasenaEmail').blur(function() {
    const email = $(this).val();
    const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

    if (!emailRegex.test(email)) {
      // El correo no es válido, deshabilita el botón de enviar
      $('#btnEnviar').prop('disabled', true);
      $('#errorEmail').text('Ingrese un correo electrónico válido').css("color", "red");
      // Agrega la clase 'error' al campo de entrada (opcional)
      $(this).addClass('error');
    } else {
      // El correo electrónico es válido, habilita el botón de enviar
      $('#btnEnviar').prop('disabled', false);
      $('#errorEmail').text('');
      $(this).removeClass('error');
    }
  });
});

//Valida que no se puedan agregar letras en los campos de precio y stock de un producto
$(document).ready(function () {
  // Validación de número en campo de precio
  $('#id_precio').on('input', function () {
      this.value = this.value.replace(/[^0-9]/g, ''); // Solo permite números
  });

  // Validación de número en campo de stock
  $('#id_stock').on('input', function () {
      this.value = this.value.replace(/[^0-9]/g, ''); // Solo permite números
  });
});