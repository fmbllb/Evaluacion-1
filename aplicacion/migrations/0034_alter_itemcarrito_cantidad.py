# Generated by Django 5.0.6 on 2024-07-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0032_producto_stock_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrito',
            name='cantidad',
            field=models.PositiveIntegerField(default=1, verbose_name='cantidad'),
        ),
    ]
