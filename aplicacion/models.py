from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from .enumeraciones import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

#from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(_("Nombre del producto"), max_length=50, unique=True)
    precio = models.IntegerField(_("Precio"), validators=[])
    descripcion = models.CharField(_("Descripción"), max_length=5000)
    categoria_producto = models.CharField(_("Categoría"), max_length=20, choices=TIPO_PRODUCTO)
    foto = models.ImageField(_("Foto"), upload_to='productos', null=True, blank=True)
    stock = models.IntegerField(_("Stock disponible"), validators=[MinValueValidator(0)], default=1)

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
    


    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Clave foránea al usuario
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
    productos = models.ManyToManyField('Producto', through='ItemCarrito', related_name='carritos')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    def agregar_producto(self, producto):
        item, creado = ItemCarrito.objects.get_or_create(carrito=self, producto=producto)
        if not creado:
            item.cantidad += 1
            item.save()

    def eliminar_producto(self, producto):
        ItemCarrito.objects.filter(carrito=self, producto=producto).delete()

    def restar_producto(self, producto):
        item = ItemCarrito.objects.get(carrito=self, producto=producto)
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
        else:
            self.eliminar_producto(producto)

    def limpiar_carrito(self):
        self.productos.clear()

    def obtener_total(self):
        total = 0
        for item in self.items.all():
            total += item.total
        return total


class ItemCarrito(models.Model):
    carrito = models.ForeignKey('Carrito', related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField('cantidad',default=1)

    @property
    def total(self):
        return self.cantidad * self.producto.precio

    def aumentar_cantidad(self):
        self.cantidad += 1
        self.save()

    def disminuir_cantidad(self):
        if self.cantidad > 1:
            self.cantidad = self.cantidad-1
            self.save()

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        self.save()

    @classmethod
    def agregar_producto(cls, carrito, producto_id, cantidad=1):
        try:
            producto = Producto.objects.get(id=producto_id)
            item, created = cls.objects.get_or_create(carrito=carrito, producto=producto)
            if not created:
                item.cantidad += cantidad
                item.save()
            return item
        except ObjectDoesNotExist:
            return None

    def eliminar(self):
        self.delete()

@receiver(post_save, sender=User)
def crear_carrito_para_usuario(sender, instance, created, **kwargs):
    if created:
        Carrito.objects.create(usuario=instance)



class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetalleCompra')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='compras')
    total = models.IntegerField(default=0)
    estado = (
        ('P', 'Pendiente'),
        ('E', 'Enviado'),
        ('R', 'Recibido'),
        ('C', 'Cancelado'),
    )
    estado_entrega = models.CharField(max_length=1, choices=estado, default='P')

    def __str__(self):
        return f'Compra de {self.usuario.username} el {self.fecha_compra}'


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle de {self.compra.usuario.username}: {self.producto.nombre}'
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

