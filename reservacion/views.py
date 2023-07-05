from django.urls import reverse
from django.shortcuts import render,get_object_or_404 , redirect
from .carro import Carro
from hotel.models import Cadena,Hotel,Oferta
from .forms import CarroAñadirProductoForm
from django.views.decorators.http import require_POST 
from .models import Reservacion, Items_Reservacion
from .forms import ReservacionForm 
from django.contrib import messages
# Create your views here.

@require_POST
def agregar_oferta(request, oferta_id):
    carro = Carro(request)
    oferta = get_object_or_404(Oferta,id=oferta_id)
    form =CarroAñadirProductoForm(request.POST, request=request, oferta = oferta_id)
    if form.is_valid():
            cd=form.cleaned_data
            carro.agregar(oferta=oferta,
                      adultos=cd['adultos'],
                      ninnos=cd['ninnos'],
                      
                      )
           
    else:
        oferta= Oferta.objects.get(id=oferta_id)
        return  render(request,'oferta.html', {'form':form, 'oferta':oferta})
    
    return redirect( reverse('detalles'))
 
@require_POST 
def carro_remove(request, oferta_id):
    carro = Carro(request)
    oferta = get_object_or_404(Oferta, id=oferta_id) 
    carro.remove(oferta)    
    return redirect('detalles')

def carro_limpiar(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect('detalles')


def carro_detalles(request):    
     carro = Carro(request)
     
     return render(request, 'carrito_detalles.html', {'carro':carro})


def crear_Reservacion(request):
    carro=Carro(request)
    transporte=False
    for item in carro:
        if item['oferta'].hotel.transporte:
            transporte=True
    if request.method =='POST':
            form= ReservacionForm(request.POST,request=request)
            transporte = False   
            if form.is_valid():
                reservacion= form.save()
                for item in carro:
                    Items_Reservacion.objects.create(reservacion=reservacion,
                                                    oferta = item['oferta'],
                                                    precio = item['precio'],
                                                    cantidad_habitaciones = item['cantidad_habitaciones'],
                                                    adultos = item['adultos'],
                                                    ninnos = item['ninnos'],
                                                    total= item['adultos']+item['ninnos']
                                                    )
                carro.limpiar()
                total=reservacion.Monto_a_pagar()
                messages.success(request,f'Reservacion guardada de forma exitosa. Total a pagar: {total} CUP. En menos de 24 horas le daremos respuestas de su sulicitud, los detalles y proceso a seguir')
                return render(request,'crear_reservacion_2.html',{'reservacion': reservacion } )
            else:
                print('no entra al is valid')
    else:
        form = ReservacionForm(request=request)
    
    return render(request,'crear_reservacion.html', {'carro':carro, 'form': form,'transporte': transporte  })


