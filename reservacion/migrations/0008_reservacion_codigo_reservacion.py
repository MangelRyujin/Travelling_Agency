# Generated by Django 4.1.2 on 2022-11-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservacion', '0007_items_reservacion_cantidad_habitaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='codigo_reservacion',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
