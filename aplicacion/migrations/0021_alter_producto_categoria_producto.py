# Generated by Django 5.0.6 on 2024-07-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0020_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_producto',
            field=models.CharField(choices=[('Miniaturas', 'Miniaturas'), ('Pinturas', 'Pinturas'), ('Accesorios', 'Accesorios')], max_length=20, verbose_name='Categoría'),
        ),
    ]
