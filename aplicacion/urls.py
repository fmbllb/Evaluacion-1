from django.urls import path
from .views import (stuff, ajustescuenta,cerrar_sesion, index, login2, crearcuenta, registro, 
    administrador, listausuarios, localizacion, catalogo, agregar_producto_carrito, carrito, contacto, 
    datospersonales, vistausuario, seguipedido, modpedido, pedidosadmin, finanzas, stock, 
    editarproducto, agregarproducto, guardado, actualizar_correo, actualizar_telefono, actualizar_usuario, detalle_producto,
    detalle_producto, eliminar_producto_carrito, eliminar_cuenta, actualizar_direccion)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrador/', administrador, name='administrador'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('carrito/', carrito, name='carrito'),
    path('catalogo/', catalogo, name='catalogo'),
    path('detalle_producto/<str:nombre_producto>/', detalle_producto, name='detalle_producto'),
    path('contacto/', contacto, name='contacto'),
    path('crearcuenta/', crearcuenta, name='crearcuenta'),
    path('ajustescuenta/<id>', ajustescuenta, name='ajustescuenta'),
    path('datospersonales/', datospersonales, name='datospersonales'),
    path('editarproducto/', editarproducto, name='editarproducto'),
    path('finanzas/', finanzas, name='finanzas'),
    path('guardado/', guardado, name='guardado'),
    path('', index, name='index'),
    #path('iniciodesesion/', iniciodesesion, name='iniciodesesion'),
    path('listausuarios/', listausuarios, name='listausuarios'),
    path('localizacion/', localizacion, name='localizacion'),
    path('modpedido/', modpedido, name='modpedido'),
    path('pedidosadmin/', pedidosadmin, name='pedidosadmin'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('registro/', registro, name='registro'),
    path('seguipedido/', seguipedido, name='seguipedido'),
    path('stock/', stock, name='stock'),
    path('vistausuario/<id>', vistausuario, name='vistausuario'),
    path('login2/', login2, name='login2'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('stuff/', stuff, name='stuff'),
    path('actualizarcorreo/', actualizar_correo, name='actualizarcorreo'),
    path('actualizarusuario/', actualizar_usuario, name='actualizarusuario'),
    path('agregarproductocarrito/<producto_id>/', agregar_producto_carrito, name='agregar_producto_carrito'),
    path('detalleproducto/<nombre_producto>/', detalle_producto, name='detalle_producto'),
    path('eliminarproductocarrito/<item_id>/', eliminar_producto_carrito, name='eliminar_producto_carrito'),
    path('actualizartelefono/', actualizar_telefono, name='actualizartelefono'),
    path('eliminar_cuenta/', eliminar_cuenta, name='eliminar_cuenta'),
    path('actualizardireccion/', actualizar_direccion, name='actualizardireccion'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)