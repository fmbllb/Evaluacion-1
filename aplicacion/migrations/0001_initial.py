# Generated by Django 5.0.6 on 2024-06-24 18:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_descuento', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Descuento')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('fecha_inicio_promo', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_fin_promo', models.DateField(verbose_name='Fecha de finalización')),
            ],
            options={
                'verbose_name': 'Promoción',
                'verbose_name_plural': 'Promociones',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la tienda')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creación')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo electrónico')),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción')),
                ('categoria_producto', models.CharField(choices=[('1', 'Electronics'), ('2', 'Clothing')], max_length=2, verbose_name='Categoría')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Foto')),
                ('fk_promocion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='aplicacion.promocion', verbose_name='Promoción')),
                ('fk_tienda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplicacion.tienda', verbose_name='Tienda')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='RUT')),
                ('nick', models.CharField(max_length=16, unique=True, verbose_name='Nombre usuario')),
                ('nombre', models.CharField(max_length=16, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=16, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo electrónico')),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('numero_casa_departamento', models.IntegerField(verbose_name='Número de Casa')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'indexes': [models.Index(fields=['nick'], name='aplicacion__nick_417b84_idx')],
            },
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Subtotal')),
                ('total', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total')),
                ('fecha_boleta', models.DateField(verbose_name='Fecha')),
                ('giro', models.CharField(choices=[('A', 'Retail'), ('B', 'Wholesale')], max_length=1, verbose_name='Giro')),
                ('medio_pago', models.CharField(choices=[('C', 'Credit Card'), ('D', 'Debit Card'), ('P', 'PayPal')], max_length=2, verbose_name='Medio de pago')),
                ('fk_producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplicacion.producto', verbose_name='Producto')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplicacion.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Boleta',
                'verbose_name_plural': 'Boletas',
            },
        ),
    ]