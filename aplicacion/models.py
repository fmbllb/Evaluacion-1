from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from .enumeraciones import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

@receiver(post_save, sender=User)
def crear_carrito_para_usuario(sender, instance, created, **kwargs):
    if created:
        Carrito.objects.create(usuario=instance)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en el carrito de {self.carrito.usuario.username}"

    def total(self):
        return self.cantidad * self.producto.precio
