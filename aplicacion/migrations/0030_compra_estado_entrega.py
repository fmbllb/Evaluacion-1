# Generated by Django 5.0.6 on 2024-07-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0029_remove_compra_carrito_compra_total_compra_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='estado_entrega',
            field=models.CharField(choices=[('P', 'Pendiente'), ('E', 'Enviado'), ('R', 'Recibido')], default='P', max_length=1),
        ),
    ]
