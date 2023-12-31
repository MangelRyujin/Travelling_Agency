# Generated by Django 4.1.2 on 2022-11-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_alter_oferta_suplemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='polo',
            field=models.CharField(choices=[('Occidente', 'occidente'), ('Centro', 'centro'), ('Oriente', 'oriente')], default='occ', max_length=9),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tipo_habitacion',
            field=models.CharField(choices=[('sencilla', 'Sencilla'), ('doble', 'Doble'), ('riple', 'Triple')], default='sencilla', max_length=8),
        ),
    ]
