from django.urls import path, include
from .views import (stuff, ajustescuenta,cerrar_sesion, index, login2, crearcuenta, registro, 
    administrador, lista_usuarios, localizacion, catalogo, agregar_producto_carrito, carrito, contacto, 
    datospersonales, vistausuario, seguipedido, modificar_estado_pedido, eliminar_pedido, listar_pedidos, finanzas, stock, 
    editarproducto, agregar_producto, actualizar_correo, actualizar_telefono, actualizar_usuario, detalle_producto,
    eliminar_producto_carrito, eliminar_cuenta, actualizar_direccion, productosadmin, eliminar_producto, autocompletar,
    detalle_producto, eliminar_producto_carrito, eliminar_cuenta, actualizar_direccion, productosadmin, eliminar_producto,
    crear_pedido, detalle_pedido, aumentar_item_carrito, disminuir_item_carrito, mis_compras,
    editar_usuario, eliminar_usuario, actualizar_direccion, crear_pedido, detalle_pedido, aumentar_item_carrito,)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrador/', administrador, name='administrador'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('carrito/', carrito, name='carrito'),
    path('catalogo/', catalogo, name='catalogo'),
    path('detalle_producto/<str:nombre_producto>/', detalle_producto, name='detalle_producto'),
    path('contacto/', contacto, name='contacto'),
    path('crearcuenta/', crearcuenta, name='crearcuenta'),
    path('ajustescuenta/<id>', ajustescuenta, name='ajustescuenta'),
    path('datospersonales/', datospersonales, name='datospersonales'),
    path('editarproducto/<str:nombre_producto>/', editarproducto, name='editarproducto'),
    path('finanzas/', finanzas, name='finanzas'),
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('productosadmin/', productosadmin, name='productosadmin'),
    path('listausuarios/', lista_usuarios, name='listausuarios'),
    path('editarusuario/<int:usuario_id>/', editar_usuario, name='editarusuario'),
    path('eliminarusuario/<int:usuario_id>/', eliminar_usuario, name='eliminarusuario'),
    path('localizacion/', localizacion, name='localizacion'),
    path('listar-pedidos/', listar_pedidos, name='listar_pedidos'),
    path('modificar_estado_pedido/<int:compra_id>/', modificar_estado_pedido, name='modificar_estado_pedido'),
    path('eliminar_pedido/<int:pedido_id>/', eliminar_pedido, name='eliminar_pedido'),
    path('detalle-pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),
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
    path('eliminar_producto/<str:nombre_producto>/', eliminar_producto, name='eliminar_producto'),
    path('actualizardireccion/', actualizar_direccion, name='actualizardireccion'),
    path('autocomplete/', autocompletar, name='autocomplete'),
    path('crear-pedido/', crear_pedido, name='crear_pedido'),
    path('detalle-pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),
    path('aumentar-item/<int:item_id>/', aumentar_item_carrito, name='aumentar_item_carrito'),
    path('disminuir-item/<int:item_id>/', disminuir_item_carrito, name='disminuir_item_carrito'),
    path('boleta/', mis_compras, name='boleta'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)