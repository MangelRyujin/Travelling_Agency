from django.contrib import admin
from .models import Items_Reservacion, Reservacion

# Register your models here.


class ReservacionItemInline(admin.TabularInline):    
    model = Items_Reservacion    
    raw_id_fields = ('oferta',)
    list_display = ('oferta.tipo_habitacion')
    readonly_fields = ('habitacion','cantidad_habitaciones')
    
    
    
    
    
@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,
                    'codigo_reservacion',
                    'carnet',
                    'estado',
                    'Total_a_pagar_de_la_reservacion',
                    'Monto_total_de_todas_las_reservaciones'
                    
                    
                     
                    
                    ]
    list_filter = ['carnet','estado', 'transporte',]
    list_per_page = 5
    list_editable = ['estado']
    search_fields = ['estado', 'transporte','carnet']
    readonly_fields= ('Total_de_personas',
                      'Total_a_pagar_de_la_reservacion',
                      'Monto_total_de_todas_las_reservaciones',
                     )
    inlines = [ReservacionItemInline,
               
               ]
 

