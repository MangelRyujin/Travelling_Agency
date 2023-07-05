from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Reservacion_Pasadia)
class Reservacion_PasadiaAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,
                    'codigo_reservacion',
                    'carnet',
                    'estado',
                    'pasadia',
                    # 'Total_a_pagar_de_la_reservacion',
                    # 'Monto_total_de_todas_las_reservaciones'
                    
                    
                     
                    
                    ]
    list_filter = ['pasadia','estado']
    list_per_page = 5
    list_editable = ['estado']
    search_fields = ['estado','pasadia']
    readonly_fields= (  'Total_de_personas',
                        'Monto_total',
                      
                     )
    # readonly_fields= ('Total_de_personas',
    #                   'Total_a_pagar_de_la_reservacion',
    #                   'Monto_total_de_todas_las_reservaciones',
    #                  )
    

@admin.register(Pasadia)
class PasadiaAdmins(admin.ModelAdmin):
    list_display = [ 'id' ,
                    'nombre',
                    'total_de_personas',
                    'Total_de_personas_en_el_viaje',
                    'Total_recaudado',
                    
                    
                    # 'Total_a_pagar_de_la_reservacion',
                    # 'Monto_total_de_todas_las_reservaciones'
                    ]
    list_filter = ['nombre']
    readonly_fields= ('Total_recaudado',
                      'Total_de_personas_en_el_viaje',
                     )