from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm
from .forms import  PerfilForm, UsuarioForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Usuario, Perfil


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

def perfil(request):
    form=PerfilForm()
    usr=request.user
    print("El ID", usr.id)
    datos={
        "form":form
    }
    existe=Perfil.objects.filter(usuario=usr.id).exists()
    print(existe)
    if request.method=="POST":
        form=PerfilForm(data=request.POST)
        if form.is_valid():
            if Perfil.objects.filter(usuario=usr).exists():
                perfil=get_object_or_404(Perfil, usuario=usr)
            else:
                perfil=Perfil()
            perfil.usuario_id=int(usr.id)
            perfil.telefono=form.cleaned_data["telefono"]
            perfil.direccion=form.cleaned_data["direccion"]
            perfil.save()
            datos["alerta"]="Datos modificados exitosamente"
    return render(request, 'aplicacion/perfil.html', datos)

def crearcuenta(request):
    form=UsuarioForm()
    if request.method=="POST":
        form=UsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente")
            return redirect(to='login2')
        else:
            messages.warning(request, "Error al crear cuenta")
            return redirect(to='crearcuenta')
    datos={
        "form":form
    }
    return render(request, 'aplicacion/registration/crearcuenta.html', datos)

def cerrar_sesion(request):
    logout(request)
    return redirect(to='index')

def usuarios(request):
    people=Usuario.objects.all()
    datos={
        "usuarios":usuarios
    }
    return render(request, 'aplicacion/usuarios.html', datos)

def login2(request):
    form=AuthenticationForm()
    datoscuenta={
        "form":form
    }
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():

            usuario=form.get_user()
            if usuario is not None:
                login(request, usuario)
                return redirect(to='index')
        else:
            print("Usuario o contraseña incorrectos")
            messages.warning(request, "Usuario o contraseña incorrectos")
            return redirect(to='login2')
    return render(request, 'aplicacion/registration/login2.html', datoscuenta)

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

"""def iniciodesesion(request):
    return render(request, 'aplicacion/registration/login.html')"""

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










