# Generated by Django 4.1.2 on 2022-11-13 04:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservacion', '0005_reservacion_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='telefono',
            field=models.TextField(default=33333333, max_length=8, validators=[django.core.validators.MinLengthValidator(8)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='carnet',
            field=models.CharField(default=33333333333, max_length=11, validators=[django.core.validators.MinLengthValidator(11)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='email',
            field=models.EmailField(blank=True, default='eduardo@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
