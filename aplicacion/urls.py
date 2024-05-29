from django.urls import path
from .views import *

urlpatterns = [
    path('administrador/', administrador, name='administrador'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('carrito/', carrito, name='carrito'),
    path('catalogo/', catalogo, name='catalogo'),
    path('contacto/', contacto, name='contacto'),
    path('datoscuenta/', datoscuenta, name='datoscuenta'),
    path('datospersonales/', datospersonales, name='datospersonales'),
    path('editarproducto/', editarproducto, name='editarproducto'),
    path('finanzas/', finanzas, name='finanzas'),
    path('guardado/', guardado, name='guardado'),
    path('', index, name='index'),
    path('iniciodesesion/', iniciodesesion, name='iniciodesesion'),
    path('listausuarios/', listausuarios, name='listausuarios'),
    path('localizacion/', localizacion, name='localizacion'),
    path('modpedido/', modpedido, name='modpedido'),
    path('pedidosadmin/', pedidosadmin, name='pedidosadmin'),
    path('producto/', producto, name='producto'),
    path('registro/', registro, name='registro'),
    path('seguipedido/', seguipedido, name='seguipedido'),
    path('stock/', stock, name='stock'),
    path('vistausuario/', vistausuario, name='vistausuario'),
]