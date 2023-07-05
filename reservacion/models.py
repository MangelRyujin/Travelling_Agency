from django.db import models
from django.core.validators import MinLengthValidator
from hotel.models import Oferta, Hotel
from datetime import date
from django.contrib import admin

# Create your models here.


class Reservacion(models.Model):
    codigo_reservacion = models.PositiveIntegerField( blank=True,  default=0)
    nombre_solicitante=models.CharField(max_length = 50,null = True)
    apellido1_solicitante=models.CharField(max_length = 50,null = True)
    apellido2_solicitante=models.CharField(max_length = 50,null = True)
    fecha_inicial=models.DateField(null = True)
    fecha_final=models.DateField(null = True)
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
    transporte = models.BooleanField(default=False) 
    
    class Meta:
        # reservacioning = ['-created']
        # indexes= [
        #     models.Index(fields=['-created']),
        # ]
        verbose_name_plural='Reservaciones'
        
    def __str__(self):        
        return f'Reservacion {self.id}'
    
    def Monto_total_de_todas_las_reservaciones(self):
        return '$ '+ str(self.Monto_total_de_las_reservaciones())+ ' CUP'
    
    
    
    def dias_min(self):
        items = Items_Reservacion.objects.all().filter(reservacion_id=self.id)
        mayor=0
        cantidad_dias= (self.fecha_final-self.fecha_inicial).days+1
        for item in items:
            cant = item.oferta.dias_min
            if mayor < cant:
                mayor = cant
        if cantidad_dias >= mayor:
            print(mayor)
            print('es mayor')
            return True
        else:
            print(mayor)
            print('es menor')       
            return False
    
    def min_a_reservar(self):
        items = Items_Reservacion.objects.all().filter(reservacion_id=self.id)
        mayor=0
        for item in items:
            cant = item.oferta.dias_min
            if mayor < cant:
                mayor = cant
        return mayor
                
            
            
            


    def Monto_total_de_las_reservaciones(self):
        reservaciones= Reservacion.objects.all().filter(estado= 'pag')
        total = 0
        for reservacion in reservaciones:
            total+=reservacion.Monto_a_pagar()
        return total    
        
    def Total_a_pagar_de_la_reservacion(self):
        return '$ '+ str(self.Monto_a_pagar())+ ' CUP'
    
    
 
    def Monto_a_pagar(self): 
        cantidad_dias= (self.fecha_final-self.fecha_inicial).days+1
        total=sum(item.get_precio() for item in self.items.all())
        total*=cantidad_dias
        cant_vier_dom=0
        sulp=0
        dias = [4,5,6]
        items = Items_Reservacion.objects.all().filter(reservacion_id=self.id)
        for item in items:
            sulp=item.oferta.hotel.precio_transporte
        for dia_ord in range(self.fecha_inicial.toordinal(),self.fecha_final.toordinal()+1):
            d=date.fromordinal(dia_ord)
            if d.weekday() in dias:
                cant_vier_dom+=1
        print(cant_vier_dom)
        if cant_vier_dom != 0:
            lineas=Items_Reservacion.objects.all().filter(reservacion_id=self.id)
            for item in lineas:
                oferta = item.oferta
                total += float(oferta.suplemento)*cant_vier_dom
        if self.transporte: 
            total+=float(sulp)
        return total
    
    def Total_de_personas(self):
        return sum(item.get_personas() for item in self.items.all())
    
class Items_Reservacion(models.Model):
    reservacion = models.ForeignKey(
        Reservacion,
        related_name= 'items',
        on_delete= models.CASCADE, 
        null = True,
        blank=True
    )
    oferta=models.ForeignKey(
        Oferta,
        related_name='items_reservacion',
        on_delete= models.CASCADE,
        null = True,
        blank=True
    )
    cantidad_habitaciones = models.PositiveIntegerField(default=0)
    precio=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    adultos = models.PositiveIntegerField(default=0, null=True)
    ninnos= models.PositiveIntegerField(default=0, null=True)
    total = models.PositiveIntegerField(default=0, null= True)
    
    def __str__(self):        
        return str(self.id)
    
    @admin.display(description='Tipo de habitacion')
    def habitacion(self):
        return self.oferta.get_tipo_habitacion_display()

    
    def get_precio(self):
        return (self.adultos* self.oferta.precio_adulto) + (self.ninnos* self.oferta.precio_primer_ninno)
    
    def get_personas(self):
        return self.adultos+self.ninnos
    #adultos*oferta.precio_adulto + ninnos * oferta.precio_primer_ninno
    
