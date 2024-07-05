from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
