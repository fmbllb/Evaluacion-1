from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from .enumeraciones import *
from django.contrib.auth.models import User
#from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(_("Nombre del producto"), max_length=50)
    precio = models.IntegerField(_("Precio"), validators=[MinValueValidator(0)])
    descripcion = models.CharField(_("Descripción"), max_length=200)
    categoria_producto = models.CharField(_("Categoría"), max_length=2, choices=TIPO_PRODUCTO)
    foto = models.ImageField(_("Foto"), upload_to='productos', null=True, blank=True)
    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
    

def __str__(self):
	return self.nombre


class Boleta(models.Model):
    subtotal = models.IntegerField(_("Subtotal"), validators=[MinValueValidator(0)])
    total = models.IntegerField(_("Total"), validators=[MinValueValidator(0)])
    fecha_boleta = models.DateField(_("Fecha"))
    giro = models.CharField(_("Giro"), max_length=1, choices=TIPO_GIRO)
    medio_pago = models.CharField(_("Medio de pago"), max_length=2, choices=TIPO_PAGO)
    fk_producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name=_("Producto"))

    class Meta:
        verbose_name = _("Boleta")
        verbose_name_plural = _("Boletas")

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(_("RUT"), max_length=10, primary_key=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

"""class Perfil(models.Model):
    rut = models.CharField(_("RUT"), max_length=10, primary_key=True)
    direccion = models.CharField(_("Dirección"), max_length=50)
    telefono = models.CharField(_("Teléfono"), max_length=9)
    """

""" class Perfil(models.Model):
        usuario = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE) 
        telefono=models.CharField(max_length=9, null=True)
        direccion=models.CharField(max_length=500, null=False)


class Usuario(models.Model):
    rut = models.CharField(_("RUT"), max_length=10, primary_key=True)
    nombre = models.CharField(_("Nombre"), max_length=16)
    apellido = models.CharField(_("Apellido"), max_length=16)
    correo = models.EmailField(_("Correo electrónico"), max_length=50, unique=True)
    numero_casa_departamento = models.IntegerField(_("Número de Casa"))
    direccion = models.CharField(_("Dirección"), max_length=50)

    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido}" """