# Generated by Django 4.1.2 on 2022-11-11 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_alter_hotel_polo'),
        ('reservacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservacion',
            options={'verbose_name_plural': 'Reservaciones'},
        ),
        migrations.AddField(
            model_name='items_reservacion',
            name='adultos',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='items_reservacion',
            name='ninnos',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='items_reservacion',
            name='oferta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_reservacion', to='hotel.oferta'),
        ),
        migrations.AddField(
            model_name='items_reservacion',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='items_reservacion',
            name='reservacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='reservacion.reservacion'),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='transporte',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='apellido1_solicitante',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='apellido2_solicitante',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='carnet',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='fecha_final',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='fecha_inicial',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='monto_a_pagar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='nombre_solicitante',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='total_de_personas',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
