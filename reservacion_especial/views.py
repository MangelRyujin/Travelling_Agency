from django.shortcuts import render
from hotel.models import Hotel, Oferta
from .models import Reservacion_Especial, Items_Reservacion_Especial
from django.core.paginator import Paginator
from datetime import date
from .forms import Reservacion_EspecialForm
from django.contrib import messages
from .models import Oferta_Especial
from django.views.decorators.http import require_POST 

# Create your views here.


def hotel_oferta_especial(request, hotel_id):
    
    hoteles=Hotel.objects.filter(id=hotel_id)
    ofertas=Oferta.objects.filter(hotel=hotel_id).exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())
    ubicacion = 'Cienfuegos'
    for hotel in hoteles:
        ubicacion = hotel.ubicacion
    otros_hoteles = Hotel.objects.all().filter(ubicacion = ubicacion).exclude(id = hotel_id)
    paginator_hotel = Paginator(otros_hoteles,3)
    page_number_hotel = request.GET.get('page')
    page_obj_hotel = paginator_hotel.get_page(page_number_hotel)    
    paginator = Paginator(ofertas, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contexto = {'oferta': ofertas, 'page_obj': page_obj,'hotel':hoteles, 'otros_hoteles':otros_hoteles , 'paginator_hotel':paginator_hotel,'page_number_hotel':page_number_hotel,'page_obj_hotel':page_obj_hotel}
    return render(request,'hotel_especial.html', contexto)

def oferta_especial(request, oferta_id):
    oferta= Oferta.objects.get(id=oferta_id)
    
    contexto = {'oferta': oferta}      
    return render(request, 'oferta_especial.html', contexto)

def reservacion_especial(request, oferta_id):
    # oferta= Oferta.objects.get(id=oferta_id)
    oferta_especial = Oferta_Especial.objects.all().exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())
    oferta_e = Oferta.objects.all().filter(id=oferta_id)
    print(oferta_e)
    if request.method=='POST':
        
        form  =   Reservacion_EspecialForm(request.POST, request = request, oferta = oferta_id)
        if form.is_valid():  
            reservacion = form.save()
            for ofert in oferta_e:
                Items_Reservacion_Especial.objects.create(
                    reservacion_especial = reservacion,
                    oferta = ofert,
                )
            total = reservacion.Monto_a_pagar()
            messages.success(request,f'Reservacion guardada de forma exitosa. Total a pagar: {total} CUP. En menos de 24 horas le daremos respuestas de su sulicitud, los detalles y proceso a seguir')
            return render(request, 'crear_reservacion_especial_2.html',{'reservacion': reservacion })
        
    else: 
        
        form = Reservacion_EspecialForm(request = request, oferta = oferta_id)
    contexto = {'oferta': oferta_e, 'form':form, 'oferta_especial':oferta_especial}      
    return render(request, 'crear_reservacion_especial.html', contexto)

# def reservar_oferta_especial(request, oferta_id, adultos, ninnos, cantidad_habitaciones):
#     oferta = Oferta.objects.filter(id = oferta_id)
#     precio_adulto = 0
#     precio_ninno = 0
#     for o in oferta:
#         precio_adulto = o.precio_adulto
#         precio_ninno = o.precio_primer_ninno
#     if request.method =='POST':
#             form= Reservacion_EspecialForm(request.POST)  
#             if form.is_valid() :
#                 reservacion= form.save()
#                 Items_Reservacion_Especial.objects.create(reservacion=reservacion,
#                                                 oferta =oferta,
#                                                 precio = adultos * precio_adulto + ninnos * precio_ninno,
#                                                 cantidad_habitaciones = cantidad_habitaciones,
#                                                 adultos = adultos,
#                                                 ninnos = ninnos,
#                                                 total= adultos + ninnos
#                                                 )
                
#                 messages.success(request,f'Reservacion guardada de forma exitosa. En menos de 24 horas le daremos respuestas de su sulicitud, los detalles y proceso a seguir')
#                 return render(request,'crear_reservacion_especial_2.html',{'reservacion': reservacion } )
#             else:
#                 print('no entra al is valid')
#     else:
#         form = Reservacion_EspecialForm()
#     return render(request,'crear_reservacion_especial.html')