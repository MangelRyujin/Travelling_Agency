# Generated by Django 4.1.2 on 2022-12-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservacion_especial', '0007_oferta_especial_precio_del_transporte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta_especial',
            name='activa',
        ),
    ]
