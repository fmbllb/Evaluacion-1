from django.contrib import admin
from .models import Perfil, Usuario, Promocion, Tienda, Producto, Boleta

# Register your models here.

class AdmPerfil(admin.ModelAdmin):
    list_display = ['usuario', 'telefono', 'direccion']

class AdmUsuario(admin.ModelAdmin):
    list_display=['rut','nombre','apellido','correo','numero_casa_departamento']
    list_filter=['rut']

admin.site.register(Usuario, AdmUsuario)
admin.site.register(Perfil, AdmPerfil)