from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from .forms import DescripcionForm

class AdmProducto(admin.ModelAdmin):
    list_display=['nombre', 'precio', 'categoria_producto']
    form=DescripcionForm


#Registro de modelos
admin.site.register(Producto, AdmProducto)