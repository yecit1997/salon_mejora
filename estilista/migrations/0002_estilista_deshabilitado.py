# Generated by Django 5.1.4 on 2025-01-11 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estilista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estilista',
            name='deshabilitado',
            field=models.BooleanField(default=False),
        ),
    ]
