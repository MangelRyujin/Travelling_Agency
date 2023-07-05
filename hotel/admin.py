from django.contrib import admin
from hotel.models import *


# Register your models here.


@admin.register(Cadena)
class CadenaAdmin(admin.ModelAdmin):
    
    list_display = [ 'nombre' ]


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [ 'nombre' , 'categoria', 'cadena', 'polo']
    list_filter = ['cadena','categoria', 'polo']
    list_per_page = 5
    list_editable = ['cadena']
    search_fields = ['nombre', 'categoria',]


#admin.site.register(Oferta)

@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = [ 'nombre' , 'tipo_habitacion', 'plan', 'hotel']
    list_filter = ['nombre','tipo_habitacion', 'plan','hotel']
    list_per_page = 5
    list_editable = ['hotel']
    search_fields = ['cadena','tipo_habitacion', 'plan','hotel']
    
@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre','email','estado']
    search_fields = ['estado']
    list_editable = ['estado']
    list_filter = ['nombre','estado']