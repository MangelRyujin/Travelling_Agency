# Generated by Django 4.1.2 on 2022-11-12 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservacion', '0003_items_reservacion_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservacion',
            name='monto_a_pagar',
        ),
        migrations.RemoveField(
            model_name='reservacion',
            name='total_de_personas',
        ),
    ]