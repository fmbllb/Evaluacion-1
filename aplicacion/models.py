from django.db import models

# Create your models here.
class Uduario(models.Model):
    rut=models.CharField("Rut", max_length=10, primary_key=True)
    nick=models.CharField("Nombre usuario", max_length=16)
    nombre=models.CharField("Nombre", max_length=16)
    apellido=models.CharField("Apellido", max_length=16)
    correo=models.EmailField("correo", max_length=50)
    contrasena=models.CharField("Contraseña", max_length=50)
    numero_casa_departamento=models.IntegerField("Numero de Casa")
    direccion=models.CharField("Direccion", max_length=50)

class Empleadxo(models.Model):
    fecha_ingreso=models.DateField("Fecha Ingreso", auto_now=False, auto_now_add=False)
    fecha_salida=models.DateField("Fecha Salida", auto_now=False, auto_now_add=False)
    salario=models.IntegerField("Salario")
    tipo_contrato=models.CharField("Contrato", max_length=1, choices=*)

class Tienda(models.Model):
    nombre=models.CharField("Nombre Tienda", max_length=50)
    direccion=models.CharField("Direccion", max_length=50)
    fecha_creacion=models.DateField("Fecha Creacion", auto_now=False, auto_now_add=False)
    telefono=models.IntegerField("Telefono")
    correo=models.CharField("Correo", max_length=50)

class Producto(models.Model):
    nombre=models.CharField("Nombre Producto", max_length=50)
    precio=models.IntegerField("Precio")
    descripcion=models.CharField("Descripcion", max_length=200)
    categoria=models.CharField("Categoria", max_length=1, choices=*)

class Boleta(models.Model):
    giro=models.CharField("Giro", max_length=1, choices=*)
    medio_pago=models.CharField("Medio Pago", max_length=2, choices=*)
    subtotal=models.IntegerField("Subtotal")
    total=models.IntegerField("Total")
    fecha_boleta=models.DateField("Fecha", auto_now=False, auto_now_add=False)

class Factura(models.Model):
    iva=models.IntegerField("IVA")
    descripcion=models.CharField("Descripcion", max_length=50)
    fecha=models.DateField("Fecha", auto_now=False, auto_now_add=False)
    descuento=models.IntegerField("Descuento")
    bruto=models.IntegerField("Bruto")

class Encuesta(models.Model):
    pregunta=models.CharField("Pregunta", max_length=50)
    respuesta=models.CharField("Respuesta", max_length=50)
    opcion=models.CharField("", max_length=5, choices=*)
    fecha_encuesta=models.DateField("Fecha", auto_now=False, auto_now_add=False)
    
class Promocion(models.Model):
    porcentaje_descuento=models.IntegerField("Descuento")
    descripcion=models.CharField("Descripcion", max_length=50)
    fecha_inicio_promo=models.DateField("Fecha Inicio", auto_now=False, auto_now_add=False)
    fecha_fin_promo=models.DateField("Fecha Fin", auto_now=False, auto_now_add=False)
