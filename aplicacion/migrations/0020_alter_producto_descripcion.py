# Generated by Django 5.0.6 on 2024-07-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0019_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
    ]