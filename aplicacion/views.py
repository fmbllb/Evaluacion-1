from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm
from .forms import *
from django.utils import timezone
from os import remove, path
from django.http import JsonResponse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .enumeraciones import TIPO_PRODUCTO

# Create your views here.

@login_required
def administrador(request):
    return render(request, 'aplicacion/administrador.html')

#VISTAS DEL PRODUCTO
@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productosadmin')
    else:
        form = AgregarProductoForm()
    return render(request, 'aplicacion/agregar_producto.html', {'form': form})


@login_required
def aumentar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.carrito.usuario != request.user:
        messages.error(request, 'No tienes permiso para modificar este ítem.')
        return redirect('carrito')
    # Debugging: print item details
    print(f"Aumentando cantidad para item: {item.id}, producto: {item.producto.nombre}")
    item.aumentar_cantidad()
    messages.success(request, f"La cantidad de {item.producto.nombre} se ha actualizado a {item.cantidad}.")
    return redirect('carrito')

@login_required
def disminuir_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.carrito.usuario != request.user:
        messages.error(request, 'No tienes permiso para modificar este ítem.')
        return redirect('carrito')
    # Debugging: print item details
    print(f"Disminuyendo cantidad para item: {item.id}, producto: {item.producto.nombre}")
    if item.cantidad > 1:
        item.disminuir_cantidad()
        messages.success(request, 'Disminuyó la cantidad del ítem.')
    else:
        messages.error(request, 'No puedes disminuir la cantidad de este ítem por debajo de 1.')
    return redirect('carrito')

@login_required
def agregar_producto_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))  # Obtener la cantidad del formulario o asignar 1 por defecto
        carrito.agregar_producto(producto, cantidad)
        messages.success(request, f"{producto.nombre} ha sido agregado al carrito.")
        return redirect('carrito')  # Redirigir a la página del carrito o donde sea necesario

    total_items = carrito.items.count()
    productos = Producto.objects.all()
    
    context = {
        'producto': producto,
        'carrito': carrito,
        'productos': productos,
        'total_items': total_items,
    }

    return render(request, 'aplicacion/carrito.html', context)


def historial_compras(request):
    return render(request, 'aplicacion/seguipedido.html')

@login_required
def actualizar_telefono(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = PhoneUpdateForm(request.POST, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu teléfono ha sido actualizado correctamente.')
            return redirect('datospersonales')  # Reemplaza 'perfil' con el nombre de tu vista de perfil
    else:
        form = PhoneUpdateForm(instance=perfil, user=request.user)

    return render(request, 'aplicacion/crud/actualizartelefono.html', {'form': form})

@login_required
def actualizar_direccion(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = DirectionUpdateForm(request.POST, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu dirección ha sido actualizada.')
            return redirect('datospersonales')
    else:
        form = DirectionUpdateForm(instance=perfil, user=request.user)

    return render(request, 'aplicacion/crud/actualizardireccion.html', {'form': form})

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
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    productos = Producto.objects.all()  #  la lista de productos que se muestran en la página de carrito
    total = sum(item.producto.precio * item.cantidad for item in carrito.items.all())
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        nueva_cantidad = int(request.POST.get('nueva_cantidad', 1))
        # Actualizar la cantidad del item en el carrito
        item = get_object_or_404(ItemCarrito, id=item_id, carrito=carrito)
        item.actualizar_cantidad(nueva_cantidad)
        # Redireccionar a la misma página o a donde desees
        return redirect('carrito')
    context = {
        'carrito': carrito,
        'productos': productos,
        'total': total,
    }
    return render(request, 'aplicacion/carrito.html', context)

def boleta(request):
    boletas_usuario = Boleta.objects.filter(usuario=request.user)
    
    context = {
        'boletas_usuario': boletas_usuario,
    }
    return render(request, 'aplicacion/boleta_usuario.html', context)

def detalle_producto(request, nombre_producto):
    producto = get_object_or_404(Producto, id=id)
    nombre_producto = producto.nombre
    context = {
        'producto': producto,
        'nombre_producto': nombre_producto
    }
    return render(request, 'aplicacion/detalleproducto.html', context)

def catalogo(request):
    productos = Producto.objects.all()

    form = FiltroCategoriaForm(request.GET)
    if form.is_valid():
        categoria = form.cleaned_data.get('categoria')
        if categoria:
            productos = productos.filter(categoria_producto=categoria)

    datos = {'productos': productos, 'form': form}

    return render(request, 'aplicacion/catalogo.html', datos)


#Detalles de producto
def detalle_producto(request, nombre_producto):

    producto = get_object_or_404(Producto, nombre=nombre_producto)
    return render(request, 'aplicacion/detalle_producto.html', {'producto': producto})



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
    request.user.delete()
    messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
    logout(request)
    return redirect(to='index')  # Redirigir a la página de inicio u otra página adecuada

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


@login_required
def finanzas(request):
    return render(request, 'aplicacion/finanzas.html')

#Index
def index(request):
    productos=Producto.objects.all()
    categorias={producto.categoria_producto: [] for producto in productos}

    for producto in productos:
        categorias[producto.categoria_producto].append(producto)

    datos = {
        'categorias': categorias,
        'productos':productos
    }
    return render(request, 'aplicacion/index.html', datos)

@login_required
def productosadmin(request):
    productos = Producto.objects.all()
    form = FiltroCategoriaForm(request.GET or None)  # Inicializa el formulario con GET o None
    
    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre_producto')
        if nombre_producto:
            producto = Producto.objects.filter(nombre=nombre_producto).first()
            if producto:
                producto.delete()
                return redirect('aplicacion/productosadmin')  # Redirige a la página de administración después de eliminar
    
    if form.is_valid():
        categoria = form.cleaned_data.get('categoria')
        if categoria:
            productos = productos.filter(categoria_producto=categoria)

    datos = {
        'productos': productos,
        'form': form,
    }
    return render(request, 'aplicacion/productosadmin.html', datos)

#Eliminar producto
def eliminar_producto(request, nombre_producto):
    producto = get_object_or_404(Producto, nombre=nombre_producto)
    producto.delete()
    return redirect('productosadmin')

#CRUD USUARIOS
@login_required
def lista_usuarios(request):
    # Obtener parámetros de orden y dirección (ascendente o descendente)
    orden_por = request.GET.get('ordenar_por', 'username')  # Campo predeterminado para ordenar
    direccion = request.GET.get('direccion', 'asc')         # Dirección predeterminada
    
    if direccion == 'desc':
        orden_por = '-' + orden_por  # Prefijo '-' para orden descendente
    
    # Obtener usuarios ordenados
    usuarios = User.objects.all().order_by(orden_por)
    
    return render(request, 'aplicacion/listausuarios.html', {
        'usuarios': usuarios,
        'orden_por': orden_por,
        'direccion': direccion
    })

def localizacion(request):
    return render(request, 'aplicacion/localizacion.html')

def modpedido(request):
    return render(request, 'aplicacion/modpedido.html')

#Editar usuario
@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listausuarios')  # Redirige a la lista de usuarios después de editar
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'aplicacion/editarusuario', {'form': form, 'usuario': usuario})

#Eliminar usuario
@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    
    if request.method == 'POST':
        # Procesar el formulario de confirmación de eliminación
        usuario.delete()
        return redirect('listausuarios')  # Redirigir a la lista de usuarios después de eliminar
    
    return render(request, 'eliminarusuario.html', {'usuario': usuario})

#CRUD DE PEDIDOS
#Crear pedidos admin
@login_required
def crear_pedido(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.producto.precio * item.cantidad for item in items)
    
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        productos_ids = request.POST.getlist('productos_ids')
        cantidades = request.POST.getlist('cantidades')

        if compra_form.is_valid() and productos_ids and cantidades:
            # Encuentra el primer producto del carrito del usuario
            producto = Producto.objects.filter(carritos__usuario=request.user).first()
            if not producto:
                return render(request, 'aplicacion/crud-pedidos/crear_pedido.html', {
                    'compra_form': compra_form,
                    'carrito': carrito,
                    'error': 'No hay productos en el carrito.'
                })

            # Encuentra la última boleta asociada a ese producto
            boleta = Boleta.objects.filter(fk_producto=producto).last()
            if not boleta:
                boleta = Boleta.objects.create(
                    subtotal=0,
                    total=0,
                    fecha_boleta=timezone.now().date(),
                    giro='',
                    medio_pago='',
                    fk_producto=producto
                )

            compra = Compra.objects.create(
                usuario=request.user,
                boleta=boleta,
                total=0
            )

            for producto_id, cantidad in zip(productos_ids, cantidades):
                producto = Producto.objects.get(id=producto_id)
                detalle = DetalleCompra(
                    compra=compra,
                    producto=producto,
                    cantidad=int(cantidad),
                    precio_unitario=producto.precio
                )
                detalle.save()
                compra.total += detalle.precio_unitario * detalle.cantidad

            compra.save()

            return redirect('listar_pedidos')

    else:
        compra_form = CompraForm()
    
    context = {
        'compra_form': compra_form,
        'carrito': carrito,
        'total': total,
        'items': items,
    }

    return render(request, 'aplicacion/crud-pedidos/crear_pedido.html', context)

#Detalle pedido
def detalle_pedido(request, id):
    compra = get_object_or_404(Compra, id=id)
    return render(request, 'aplicacion/crud-pedidos/detalle_pedido.html', {'compra': compra})

#Listar Pedidos
@login_required
def listar_pedidos(request):
    compras = Compra.objects.all().order_by('-fecha_compra')
    context = {
        'compras': compras
    }
    return render(request, 'aplicacion/crud-pedidos/listar_pedidos.html', context)



def registro(request):
    return render(request, 'aplicacion/registro.html')


@login_required
def stock(request):
    return render(request, 'aplicacion/stock.html')

#Editar un producto existente
def editarproducto(request, nombre_producto):
    produc=get_object_or_404(Producto,nombre= nombre_producto)
    form=EditarProductoForm(instance=produc)
    imagen_anterior = produc.foto.path if produc.foto else None
    
    if request.method=="POST":
            form=EditarProductoForm(data=request.POST,files=request.FILES,instance=produc)
            if form.is_valid():
                imagen_nueva = form.cleaned_data.get('foto') if len(form.cleaned_data.get('foto').name.split("/")) == 1 else None
                if imagen_nueva and imagen_anterior:
                # Comprobar si la nueva imagen es diferente de la anterior
                    if imagen_nueva.name != path.basename(imagen_anterior):
                    # Eliminar la imagen anterior
                        if path.exists(imagen_anterior):
                            remove(imagen_anterior)
                    
                form.save()
                return redirect(to="productosadmin")
                
    datos={
        "form":form ,
        "producto":produc
    }
    
    return render(request,'aplicacion/editarproducto.html',datos)
    

#Eliminar producto
@login_required
def eliminar_producto(request, nombre_producto):
    producto = get_object_or_404(Producto, nombre=nombre_producto)
    if request.method == 'POST' and request.POST.get('eliminar') == 'True':
        # Eliminar la imagen asociada al producto si existe
        if producto.foto:
            producto.foto.delete()
        # Eliminar el producto de la base de datos
        producto.delete()
        return redirect('productosadmin')  # Redirige a la página de administración de productos después de eliminar

    # Si no se confirma la eliminación, redirige a la página de edición del producto
    return redirect('editar_producto', nombre_producto=nombre_producto)

#Autocompletado barra de busqueda
def autocompletar(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        productos = Producto.objects.filter(nombre__icontains=term)
        results = []
        for producto in productos:
            producto_json = {}
            producto_json['label'] = producto.nombre
            producto_json['value'] = reverse('detalle_producto', args=[producto.nombre])
            results.append(producto_json)
        return JsonResponse(results, safe=False)