# Generated by Django 5.0.6 on 2024-07-04 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0018_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre del producto'),
        ),
    ]
