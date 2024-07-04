from django.db import migrations, models

def set_default_ids(apps, schema_editor):
    Perfil = apps.get_model('aplicacion', 'Perfil')
    for perfil in Perfil.objects.all():
        if perfil.id is None:
            perfil.id = None  # Deja que Django asigne el valor
            perfil.save()

class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_perfil_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='foto_perfil',
        ),
        migrations.AddField(
            model_name='perfil',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_ids, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='perfil',
            name='rut',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
