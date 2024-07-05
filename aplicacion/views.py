from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm  
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, ItemCarrito, Compra
#importando desde forms, los formularios
from .forms import UsuarioForm, EmailUpdateForm, UserUpdateForm

# Create your views here.

def administrador(request):
    return render(request, 'aplicacion/administrador.html')




#VISTAS DEL PRODUCTO
@login_required
def agregarproducto(request):
    return render(request, 'aplicacion/agregarproducto.html')

@login_required
def agregar_producto_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))  # Obtener la cantidad del formulario o asignar 1 por defecto
        carrito.agregar_producto(producto, cantidad)
        messages.success(request, f"{producto.nombre} ha sido agregado al carrito.")
        return redirect('carrito')

    total_items = carrito.items.count()
    productos = Producto.objects.all()
    
    context = {
        'producto': producto,
        'carrito': carrito,
        'productos': productos,
        'total_items': total_items,
    }

    return render(request, 'aplicacion/carrito.html', context)

def actualizar_telefono(request):
    return render(request, 'aplicacion/crud/actualizartelefono.html')

@login_required
def eliminar_producto_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.carrito.usuario != request.user:
        return redirect('carrito')  # Redirige si no tiene permisos
    
    # Elimina el item del carrito
    item.eliminar()
    
    messages.success(request, f"{item.producto.nombre} ha sido eliminado del carrito.")
    return redirect('carrito')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'aplicacion/carrito.html', {'productos': productos})

@login_required
def seguipedido(request):
    compras = Compra.objects.filter(carrito__usuario=request.user).order_by('-fecha_compra')
    return render(request, 'aplicacion/seguipedido.html', {'compras': compras})

@login_required
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    
    if not carrito:
        # Si el usuario no tiene un carrito, podemos crear uno nuevo
        carrito = Carrito.objects.create(usuario=request.user)
    
    total_items = carrito.items.count()
    productos = Producto.objects.all()
    
    context = {
        'carrito': carrito,
        'total_items': total_items,
        'productos': productos,
    }
    return render(request, 'aplicacion/carrito.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {
        'producto': producto,
    }
    return render(request, 'aplicacion/detalleproducto.html', context)

def catalogo(request):
    return render(request, 'aplicacion/catalogo.html')



#VISTA DE CONTACTO
def contacto(request):
    return render(request, 'aplicacion/contacto.html')
#futuro formulario de perfil
""" def perfil():
    return render() """

@login_required
def stuff(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticación del usuario
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('index')
        else:
            # Manejo de errores de autenticación
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'aplicacion/stuff.html', {'form': form})


#VISTAS DE USUARIO/CUENTA

def crearcuenta(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente")
            return redirect('login2')
        else:
            messages.warning(request, "Error al crear cuenta")
    else:
        form = UsuarioForm()

    return render(request, 'aplicacion/registration/crearcuenta.html', {'form': form})

def login2(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticación del usuario
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('index')
        else:
            # Manejo de errores de autenticación
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'aplicacion/registration/login2.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect(to='index')

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
        logout(request)
        return redirect('home')  # Redirigir a la página de inicio u otra página adecuada

    return render(request, 'aplicacion/eliminar_cuenta.html')

@login_required
#ajustescuenta--------------------------------------------------------------------------------------------------------------------
def ajustescuenta(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
        datos = {
            'form': form,
            'usuario': usuario
        }
        return render(request, 'aplicacion/crud/ajustescuenta.html', datos)
    else:
        # Aquí puedes agregar el manejo del POST, por ejemplo:
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Redirigir a otra página o mostrar un mensaje de éxito
            return redirect('nombre_de_la_vista_a_redirigir')  # Cambia 'nombre_de_la_vista_a_redirigir' por el nombre adecuado
        else:
            datos = {
                'form': form,
                'usuario': usuario
            }
            return render(request, 'aplicacion/crud/ajustescuenta.html', datos)

@login_required
def vistausuario(request, id):
    usuario = get_object_or_404(User, id=id)
    context = {
        'usuario': usuario
    }
    return render(request, 'aplicacion/vistausuario.html', context)

@login_required
def datospersonales(request):
    return render(request, 'aplicacion/crud/datospersonales.html')

@login_required
def actualizar_correo(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'Correo actualizado exitosamente')
            return redirect('datospersonales')  # Reemplaza con tu URL de redirección correcta
        else:
            messages.error(request, 'Error al actualizar correo')
    else:
        form = EmailUpdateForm(instance=request.user, user=request.user)
    
    return render(request, 'aplicacion/crud/actualizarcorreo.html', {
        'form': form
    })

@login_required
def actualizar_usuario(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente')
            return redirect('datospersonales')  # Reemplaza con tu URL de redirección correcta
        else:
            messages.error(request, 'Error al actualizar usuario. Por favor, corrija los errores.')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'aplicacion/crud/actualizarusuario.html', {
        'form': form
    })

def editarproducto(request):
    return render(request, 'aplicacion/editarproducto.html')

def finanzas(request):
    return render(request, 'aplicacion/finanzas.html')

def guardado(request):
    return render(request, 'aplicacion/guardado.html')

def index(request):
    return render(request, 'aplicacion/index.html')

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


def stock(request):
    return render(request, 'aplicacion/stock.html')

