# Generated by Django 4.1.2 on 2022-11-14 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0019_alter_contacto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
