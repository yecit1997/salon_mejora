# Generated by Django 5.1.4 on 2025-01-18 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estilista', '0008_remove_estilista_rol_estilista_rol'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estilista',
            options={'ordering': ['-fecha_creacion'], 'permissions': (('puede_ver_listas', 'Puede ver las listas'),), 'verbose_name': 'estilista', 'verbose_name_plural': 'estilistas'},
        ),
    ]
