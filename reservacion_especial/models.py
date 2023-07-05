from django.db import models
from hotel.models import Hotel, Oferta
from django.contrib import admin
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date

# Create your models here.

class Oferta_Especial(models.Model):
    nombre = models.CharField(max_length = 50,null = True)
    fecha_inicial_vigente = models.DateField(null = True)
    fecha_final_vigente = models.DateField(null = True)
    fecha_inicial=models.DateField(null = True)
    fecha_final=models.DateField(null = True)
    total_de_personas = models.PositiveIntegerField(null = False, default=0)
    precio_del_transporte=models.DecimalField(max_digits=10,decimal_places=2,default=0, validators=[MinValueValidator(0)])
    
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='ofertas_especiales')
    
    class Meta:
        verbose_name_plural='Ofertas especiales'
        
    def __str__(self):        
        return self.nombre
    
    def cantidad_dias(self):
        return (self.fecha_final - self.fecha_inicial).days + 1
    
    def Total_recaudado(self):
        return '$ '+ str(self.Monto_total())+ ' CUP'
    
    def Faltan(self):
        return self.total_de_personas - self.Total_de_personas_en_el_viaje()
    
    def Total_de_personas_en_el_viaje(self):
        reservaciones = Reservacion_Especial.objects.all().filter(oferta_especial = self.id).filter(estado='pag')
        total = 0
        for r in reservaciones:
            total += r.Total_de_personas()
        return total   
    
    def Monto_total(self):
        reservaciones = Reservacion_Especial.objects.all().filter(oferta_especial = self.id).filter(estado='pag')
        monto = 0
        for r in reservaciones:
            monto += r.Monto_a_pagar() 
        return monto
    
class Reservacion_Especial(models.Model):
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
    oferta_especial = models.ForeignKey(Oferta_Especial, on_delete=models.CASCADE, related_name='oferta_especial') 
    cantidad_habitaciones = models.PositiveIntegerField(default=0)
    adultos = models.PositiveIntegerField(default=0, null=True)
    ninnos= models.PositiveIntegerField(default=0, null=True)
    
    class Meta:
        # reservacioning = ['-created']
        # indexes= [
        #     models.Index(fields=['-created']),
        # ]
        verbose_name_plural='Reservaciones especiales'
        
    def __str__(self):        
        return f'Reservacion especial {self.id}'
    
    def Monto_a_pagar(self): 
        cantidad_dias= self.oferta_especial.cantidad_dias()
        sulp = 0
        cant_vier_dom=0
        dias = [4,5,6]
        total = 0
        items = Items_Reservacion_Especial.objects.all().filter(reservacion_especial_id=self.id)
        for item in items:
            sulp = item.oferta.suplemento
            total = item.oferta.precio_adulto*self.adultos + item.oferta.precio_primer_ninno*self.ninnos
        for dia_ord in range(self.oferta_especial.fecha_inicial.toordinal(),self.oferta_especial.fecha_final.toordinal()+1):
            d=date.fromordinal(dia_ord)
            if d.weekday() in dias:
                cant_vier_dom+=1
        return float(total)*cantidad_dias + float(sulp)*cant_vier_dom + float(self.oferta_especial.precio_del_transporte)    
       
    
    def Total_de_personas(self):
        return self.adultos + self.ninnos
    
    def Monto_total(self):
        return '$ '+ str(self.Monto_a_pagar())+ ' CUP'
        
class Items_Reservacion_Especial(models.Model):
    reservacion_especial = models.ForeignKey(
        Reservacion_Especial,
        related_name= 'items_especial',
        on_delete= models.CASCADE, 
        null = True,
        blank=True
    )
    oferta=models.ForeignKey(
        Oferta,
        related_name='items_reservacion_especial',
        on_delete= models.CASCADE,
        null = True,
        blank=True
    )
    
    
    def __str__(self):        
        return str(self.id)
    
    def Tipo_de_habitacion(self):
        return self.oferta.tipo_habitacion