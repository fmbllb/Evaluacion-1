# Generated by Django 5.0.6 on 2024-07-05 08:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0028_merge_20240705_0423'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='carrito',
        ),
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productos',
            field=models.ManyToManyField(through='aplicacion.DetalleCompra', to='aplicacion.producto'),
        ),
    ]