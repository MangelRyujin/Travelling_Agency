from django.contrib import admin
from .models import *

# Register your models here.


class Reservacion_Especial_ItemInline(admin.TabularInline):    
    model = Items_Reservacion_Especial   
    raw_id_fields = ('oferta',)
    readonly_fields = ('Tipo_de_habitacion',)
    
    
    
    
    
    
    
@admin.register(Reservacion_Especial)
class Reservacion_EspecialAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,
                    'codigo_reservacion',
                    'carnet',
                    'estado',
                    'oferta_especial',
                    # 'Total_a_pagar_de_la_reservacion',
                    # 'Monto_total_de_todas_las_reservaciones'
                    
                    
                     
                    
                    ]
    list_filter = ['oferta_especial','estado']
    list_per_page = 5
    list_editable = ['estado']
    search_fields = ['estado','oferta_especial']
    readonly_fields= (  'Total_de_personas',
                        'Monto_total',
                      
                     )
    # readonly_fields= ('Total_de_personas',
    #                   'Total_a_pagar_de_la_reservacion',
    #                   'Monto_total_de_todas_las_reservaciones',
    #                  )
    inlines = [Reservacion_Especial_ItemInline,
               
               ]

@admin.register(Oferta_Especial)
class Oferta_Especial(admin.ModelAdmin):
    list_display = [ 'id' ,
                    'nombre',
                    
                    'hotel',
                    'Total_recaudado',
                    'Total_de_personas_en_el_viaje',
                    
                    # 'Total_a_pagar_de_la_reservacion',
                    # 'Monto_total_de_todas_las_reservaciones'
                    ]
    list_filter = ['nombre']
    readonly_fields= ('Total_recaudado',
                      'Total_de_personas_en_el_viaje',
                     )