# Generated by Django 5.0.6 on 2024-07-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0035_merge_20240709_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estado_entrega',
            field=models.CharField(choices=[('P', 'Pendiente'), ('E', 'Enviado'), ('R', 'Recibido'), ('C', 'Cancelado')], default='P', max_length=1),
        ),
    ]