from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

class AdmProducto(admin.ModelAdmin):
    list_display=['nombre', 'precio', 'categoria_producto']


#Registro de modelos
admin.site.register(Producto, AdmProducto)