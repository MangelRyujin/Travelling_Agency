from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from datetime import date
from django.contrib import admin

# Create your models here.
class Pasadia(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    fecha = models.DateField()
    fecha_inicial_vigente = models.DateField()
    fecha_final_vigente = models.DateField()
    total_de_personas = models.PositiveIntegerField(null = False, default=0)
    precio_adulto=models.DecimalField(max_digits=10,decimal_places=2,default=0, validators=[MinValueValidator(0)])
    precio_ninno=models.DecimalField(max_digits=10,decimal_places=2,default=0, validators=[MinValueValidator(0)])
    plan= models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to = "pasadia" , null= True)
    
    class Meta:
        verbose_name_plural='Pasadía'
        
    def __str__(self):        
        return self.nombre
    
    def Total_recaudado(self):
        return '$ '+ str(self.Monto_total())+ ' CUP'
    
    def Faltan(self):
        return self.total_de_personas - self.Total_de_personas_en_el_viaje()
    
    def Total_de_personas_en_el_viaje(self):
        reservaciones = Reservacion_Pasadia.objects.all().filter(pasadia = self.id).filter(estado='pag')
        total = 0
        for r in reservaciones:
            total += r.Total_de_personas()
        return total   
    
    def Monto_total(self):
        reservaciones = Reservacion_Pasadia.objects.all().filter(pasadia = self.id).filter(estado='pag')
        monto = 0
        for r in reservaciones:
            monto += r.Monto_a_pagar() 
        return monto
    
    
class Reservacion_Pasadia(models.Model):
    codigo_reservacion = models.PositiveIntegerField( blank=True,  default=0)
    nombre_solicitante=models.CharField(max_length = 50,null = True)
    apellido1_solicitante=models.CharField(max_length = 50,null = True)
    apellido2_solicitante=models.CharField(max_length = 50,null = True) 
    carnet=models.CharField( max_length=11,validators=[MinLengthValidator(11)])
    email=models.EmailField(blank=True)
    telefono=models.TextField(max_length=8,validators=[MinLengthValidator(8)])
    estados = [
        ('env', 'Enviada'),
        ('ace', 'Aceptada'),
        ('can', 'Cancelada'),
        ('pag', 'Pagada')
    ]
    estado= models.CharField(choices = estados, default= 'env', null = False , max_length=3)
    pasadia = models.ForeignKey(Pasadia, on_delete=models.CASCADE, related_name='pasadia') 
    
    adultos = models.PositiveIntegerField(default=0, null=True)
    ninnos= models.PositiveIntegerField(default=0, null=True)
    
    class Meta:
        # reservacioning = ['-created']
        # indexes= [
        #     models.Index(fields=['-created']),
        # ]
        verbose_name_plural='Reservaciones de pasadía'
        
    def __str__(self):        
        return f'Reservacion {self.id}'
    
    def Monto_a_pagar(self): 
        pasadia = Pasadia.objects.all().filter(id= self.pasadia.id)
        a = 0
        n = 0
        for p in pasadia:
            a = p.precio_adulto
            n = p.precio_ninno
        return self.adultos*a + self.ninnos*n
        
    def Total_de_personas(self):
        return self.adultos + self.ninnos
    
    def Monto_total(self):
        return '$ '+ str(self.Monto_a_pagar())+ ' CUP'