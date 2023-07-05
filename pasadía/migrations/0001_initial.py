# Generated by Django 4.1.2 on 2022-12-15 12:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('fecha_inicial_vigente', models.DateField()),
                ('fecha_final_vigente', models.DateField()),
                ('total_de_personas', models.PositiveIntegerField(default=0)),
                ('precio_adulto', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('precio_ninno', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('plan', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Pasadía',
            },
        ),
        migrations.CreateModel(
            name='Reservacion_Pasadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_reservacion', models.PositiveIntegerField(blank=True, default=0)),
                ('nombre_solicitante', models.CharField(max_length=50, null=True)),
                ('apellido1_solicitante', models.CharField(max_length=50, null=True)),
                ('apellido2_solicitante', models.CharField(max_length=50, null=True)),
                ('carnet', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.TextField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('estado', models.CharField(choices=[('env', 'Enviada'), ('ace', 'Aceptada'), ('can', 'Cancelada'), ('pag', 'Pagada')], default='env', max_length=3)),
                ('cantidad_habitaciones', models.PositiveIntegerField(default=0)),
                ('adultos', models.PositiveIntegerField(default=0, null=True)),
                ('ninnos', models.PositiveIntegerField(default=0, null=True)),
                ('pasadia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasadia', to='pasadía.pasadia')),
            ],
            options={
                'verbose_name_plural': 'Reservaciones de pasadía',
            },
        ),
    ]
