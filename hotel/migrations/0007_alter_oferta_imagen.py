# Generated by Django 4.1.2 on 2022-11-01 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_oferta_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='oferta'),
        ),
    ]
