from django.shortcuts import render

# Create your views here.

def administrador(request):
    return render(request, 'aplicacion/administrador.html')

def agregarproducto(request):
    return render(request, 'aplicacion/agregarproducto.html')

def carrito(request):
    return render(request, 'aplicacion/carrito.html')

def catalogo(request):
    return render(request, 'aplicacion/catalogo.html')

def contacto(request):
    return render(request, 'aplicacion/contacto.html')

def datoscuenta(request):
    return render(request, 'aplicacion/datoscuenta.html')

def datospersonales(request):
    return render(request, 'aplicacion/datospersonales.html')

def editarproducto(request):
    return render(request, 'aplicacion/editarproducto.html')

def finanzas(request):
    return render(request, 'aplicacion/finanzas.html')

def guardado(request):
    return render(request, 'aplicacion/guardado.html')

def index(request):
    return render(request, 'aplicacion/index.html')

def iniciodesesion(request):
    return render(request, 'aplicacion/iniciodesesion.html')

def listausuarios(request):
    return render(request, 'aplicacion/listausuarios.html')

def localizacion(request):
    return render(request, 'aplicacion/localizacion.html')

def modpedido(request):
    return render(request, 'aplicacion/modpedido.html')

def pedidosadmin(request):
    return render(request, 'aplicacion/pedidosadmin.html')

def producto(request):
    return render(request, 'aplicacion/producto.html')

def registro(request):
    return render(request, 'aplicacion/registro.html')

def seguipedido(request):
    return render(request, 'aplicacion/seguipedido.html')

def stock(request):
    return render(request, 'aplicacion/stock.html')

def vistausuario(request):
    return render(request, 'aplicacion/vistausuario.html')










