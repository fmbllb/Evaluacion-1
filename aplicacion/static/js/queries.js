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

//Valida los campos de "Editar Producto"
$(document).ready(function() {
  function validarCampos() {
    let nombreProducto = $("#nombreProducto").val();
    let descripcionProducto = $("#descripcionProducto").val();
    let precioProducto = $("#precioProducto").val();
    let categoriaProducto = $("#categoriaProducto").val();
    let imagenProducto = $("#imagenProducto").val();

    if (nombreProducto !== "" && descripcionProducto !== "" && precioProducto !== "" && categoriaProducto !== "" && imagenProducto !== "") {
      // Todos los campos están llenos
      if (!precioProducto.includes('-')) {
        // El precio no contiene "-"
        $("#btnGuardarCambios").prop("disabled", false);
        $("#mensajePrecio").text(""); // Borra el mensaje de error
      } else {
        // El precio contiene "-", por lo que no permitimos agregar el producto
        $("#btnGuardarCambios").prop("disabled", true);
        $("#mensajePrecio").text("No se pueden ingresar valores negativos en el precio del producto.").css("color", "red");
      }
    } else {
      // No todos los campos están llenos
      $("#btnGuardarCambios").prop("disabled", true);
      $("#mensajePrecio").text(""); // Borra el mensaje de error si los campos no están llenos
    }
  }

  // Llama a la función validarCampos cuando se cambia el valor de cualquier campo
  $("#nombreProducto, #descripcionProducto, #precioProducto, #categoriaProducto, #imagenProducto").on("input", validarCampos);
});

//Elimina elemento de la lista de los pedidos del administrador
$(document).ready(function() {
  $("#confirmacionEliminarPedido").click(function() {
      // Esconde los elementos en el div con id "contenedor"
      $("#pedido1Admin").children().hide();
  });
});

//Pagina carrito
// Script jQuery para calcular el precio total del carrito
$(document).ready(function() {
  // Función para actualizar el precio total cuando cambia la cantidad
  $('.item-quantity').on('input', function() {
      var itemId = $(this).data('item-id');
      var cantidad = parseInt($(this).val());
      
      // Obtener el precio unitario del producto desde el modelo Producto
      var precioUnitario = parseFloat($('#precioTotal-' + itemId).data('precio-unitario'));
      
      // Verificar si el precioUnitario es un número válido y mayor que cero
      if (isNaN(precioUnitario) || precioUnitario <= 0) {
          precioUnitario = 0; // Establecer un valor predeterminado si no es válido
      }
      
      // Calcular el precio total del item
      var precioTotalItem = cantidad * precioUnitario;
      
      // Actualizar el texto del precio total del item en el carrito
      $('#precioTotal-' + itemId).text('$' + precioTotalItem.toFixed(2));
      
      // Calcular y actualizar el precio total del carrito
      calcularPrecioTotalCarrito();
  });

  // Función para manejar el incremento de cantidad
  $('.btn-plus').on('click', function() {
      var itemId = $(this).data('item-id');
      var inputCantidad = $('.item-quantity[data-item-id="' + itemId + '"]');
      var cantidad = parseInt(inputCantidad.val());
      cantidad++;
      inputCantidad.val(cantidad).trigger('input');
  });

  // Función para manejar el decremento de cantidad
  $('.btn-minus').on('click', function() {
      var itemId = $(this).data('item-id');
      var inputCantidad = $('.item-quantity[data-item-id="' + itemId + '"]');
      var cantidad = parseInt(inputCantidad.val());
      if (cantidad > 1) {
          cantidad--;
          inputCantidad.val(cantidad).trigger('input');
      }
  });

  // Deshabilitar la edición manual de los inputs de cantidad
  $('.item-quantity').prop('disabled', true);

  // Función para calcular el precio total del carrito
  function calcularPrecioTotalCarrito() {
      var totalCarrito = 0;
      
      // Iterar sobre cada item en el carrito y sumar sus precios totales
      $('.item-quantity').each(function() {
          var itemId = $(this).data('item-id');
          var cantidad = parseInt($(this).val());
          var precioUnitario = parseFloat($('#precioTotal-' + itemId).data('precio-unitario'));
          
          // Verificar si el precioUnitario es un número válido y mayor que cero
          if (isNaN(precioUnitario) || precioUnitario <= 0) {
              precioUnitario = 0; // Establecer un valor predeterminado si no es válido
          }
          
          var precioTotalItem = cantidad * precioUnitario;
          totalCarrito += precioTotalItem;
      });
      
      // Actualizar el texto del precio total del carrito en el HTML
      $('#totalCarrito').text('Total: $' + totalCarrito.toFixed(2));
  }

  // Llamar a la función para calcular el precio total del carrito al cargar la página
  calcularPrecioTotalCarrito();
});



$(document).ready(function() {
  // Función para el botón de aumentar cantidad
  $('.qtyInputCarrito').on('click', '.btn.plus', function(e) {
      e.preventDefault();
      var input = $(this).closest('.qtyInputCarrito').find('input');
      var newValue = parseInt(input.val()) + 1;
      input.val(newValue);
      actualizarPrecioTotal(input); // Llama a la función para actualizar el precio total
  });

  // Función para el botón de disminuir cantidad
  $('.qtyInputCarrito').on('click', '.btn.minus', function(e) {
      e.preventDefault();
      var input = $(this).closest('.qtyInputCarrito').find('input');
      var newValue = parseInt(input.val()) - 1;
      if (newValue < 1) {
          newValue = 1;
      }
      input.val(newValue);
      actualizarPrecioTotal(input); // Llama a la función para actualizar el precio total
  });

  // Función para actualizar el precio total de un ítem
  function actualizarPrecioTotal(input) {
      var cantidad = parseInt(input.val());
      var precioUnitario = parseFloat(input.closest('.card-body').find('.precio-unitario').text());
      var precioTotal = cantidad * precioUnitario;
      input.closest('.card-body').find('.precio-total').text(precioTotal.toFixed(2));
      input.closest('.card-body').find('.precio-total-hidden').val(precioTotal.toFixed(2));
      actualizarTotalCarrito(); // Actualiza el precio total del carrito
  }

  // Función para actualizar el precio total del carrito
  function actualizarTotalCarrito() {
      var totalCarrito = 0;
      $('.precio-total').each(function() {
          totalCarrito += parseFloat($(this).text());
      });
      $('#totalCarrito').text('Total: $' + totalCarrito.toFixed(2));
  }

  // Llamar a actualizarTotalCarrito al cargar la página
  actualizarTotalCarrito();
});


/*$(document).ready(function () {
  let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

  // Lógica para validar una dirección de correo electrónico
  $("#registroForm").submit(function (event) {
    // Evitar que se envíe el formulario por defecto
    event.preventDefault();

    // Obtener el valor del campo de correo electrónico
    let email = $("#registroEmail").val();

    // Validar el correo electrónico usando la expresión regular
    if (emailRegex.test(email)) {
      // El correo electrónico es válido
      alert("Correo electrónico válido.");
    } else {
      // El correo electrónico no es válido
      alert("Correo electrónico inválido.");
    }
  });
});*/
