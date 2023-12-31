# Generated by Django 4.1.2 on 2022-11-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_oferta_cant_max_adulto_oferta_cant_max_ninnos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='cant_max_adulto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='cant_max_ninnos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='cant_min_adulto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='cant_min_ninnos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tipo_habitacion',
            field=models.CharField(choices=[('sencilla', 'Sencilla'), ('doble', 'Doble'), ('triple', 'Triple')], default='sencilla', max_length=8),
        ),
    ]
