from django.urls import path
from .views import (stuff, ajustescuenta,cerrar_sesion, index, login2, crearcuenta, registro, 
    administrador, listausuarios, localizacion, catalogo, producto, carrito, contacto, 
    datospersonales, vistausuario, seguipedido, modpedido, pedidosadmin, finanzas, stock, 
    editarproducto, agregarproducto, guardado, actualizar_correo, actualizar_usuario)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrador/', administrador, name='administrador'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('carrito/', carrito, name='carrito'),
    path('catalogo/', catalogo, name='catalogo'),
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
    path('producto/', producto, name='producto'),
    path('registro/', registro, name='registro'),
    path('seguipedido/', seguipedido, name='seguipedido'),
    path('stock/', stock, name='stock'),
    path('vistausuario/<id>', vistausuario, name='vistausuario'),
    path('login2/', login2, name='login2'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('stuff/', stuff, name='stuff'),
    path('actualizarcorreo/', actualizar_correo, name='actualizarcorreo'),
    path('actualizarusuario/', actualizar_usuario, name='actualizarusuario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)