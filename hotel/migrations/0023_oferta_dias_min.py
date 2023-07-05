# Generated by Django 4.1.2 on 2022-11-17 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0022_contacto_estado_alter_oferta_tipo_habitacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='dias_min',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
    ]
