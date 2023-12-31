# Generated by Django 4.1.2 on 2022-11-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0021_alter_contacto_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Respondidos', 'Respondidos')], default='Pendiente', max_length=11),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tipo_habitacion',
            field=models.CharField(choices=[('sencilla', 'Sencilla'), ('doble', 'Doble'), ('triple', 'Triple')], default='sencilla', max_length=8),
        ),
    ]
