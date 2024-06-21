from django.contrib import admin
from .models import Usuario
# Register your models here.
class AdmUsuario(admin.ModelAdmin):
    list_display= ['rut','nick','nombre','apellido','correo']
