from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from turtle import mode
from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator
from datetime import datetime
from decimal import Decimal



# Create your models here.

class Cadena(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

    

class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    polo = [
        ('Occidente', 'occidente'),
        ('Centro', 'centro'),
        ('Oriente', 'oriente')
    ]
    polo = models.CharField(max_length = 9 , choices = polo, default= 'occ', null = False )
    descripcion = models.TextField()
    categoria =  models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)],
        help_text='Cantidad de estrellas entre 1 y 5'
        )
    #image =  models.ImageField()
    activo = models.BooleanField(default=False)
    transporte = models.BooleanField(default=False)
    precio_transporte=models.DecimalField(max_digits=10 , decimal_places=2,null = True, default=0)
    cadena = models.ForeignKey(Cadena, on_delete=models.CASCADE,related_name='hoteles')
    imagen = models.ImageField(upload_to = "hotel" , null= True)
    url= models.TextField(blank=True)

    class Meta:
        verbose_name_plural='hoteles'

    def __str__(self) -> str:
        return self.nombre
    
    def estrellas(self):
        return [i for i in range(int(self.categoria))]
    
    def transporte_precio(self):
        return self.precio_transporte
    
    
class Oferta(models.Model):
    habitaciones = [
        ('sencilla', 'Sencilla'),
        ('doble', 'Doble'),
        ('triple', 'Triple')
    ]
    nombre = models.CharField(max_length=50)
    plan= models.CharField(max_length=20)
    dias_min = models.PositiveSmallIntegerField(default=0, )
    fecha_inicial_vigente = models.DateField()
    fecha_final_vigente = models.DateField()
    fecha_inicial_reserva = models.DateField()
    fecha_final_reserva = models.DateField()
    tipo_habitacion = models.CharField(max_length = 8 , choices = habitaciones, default= 'sencilla', null = False )
    precio_adulto = models.FloatField()
    precio_primer_ninno = models.FloatField()
    suplemento  = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to = "oferta" , null= True , default='oferta/3.png')
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='ofertas')
    cant_min_adulto= models.IntegerField(null = True)
    cant_max_adulto= models.IntegerField(null = True)
    cant_min_ninnos= models.IntegerField(null = True)
    cant_max_ninnos= models.IntegerField(null = True)
    
    def __str__(self) -> str:
        return self.nombre
    
    
        

    class Meta:
        verbose_name_plural='ofertas'
       

class Contacto(models.Model):
    estados = [
        ('Pendiente', 'Pendiente'),
        ('Respondidos', 'Respondidos'),
    ]
    nombre = models.CharField(max_length=50)
    email=models.EmailField(null=False)
    mensaje=models.TextField()
    estado= models.CharField(max_length = 11 , choices = estados, default= 'Pendiente', null = False )
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='contactos'