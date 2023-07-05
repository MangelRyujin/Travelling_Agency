from django.shortcuts import render
from .models import *
from .forms import Reservacion_PasadiaForm
from django.contrib import messages
# Create your views here.


def pasadia(request, pasadia_id):
    pasadia= Pasadia.objects.get(id=pasadia_id)
    pas = Pasadia.objects.all().filter(id=pasadia_id)
    if request.method=='POST':
        
        form  =   Reservacion_PasadiaForm(request.POST,request=request, pasadia = pasadia_id)
        if form.is_valid():  
            reservacion = form.save()
            total = reservacion.Monto_a_pagar()
            messages.success(request,f'Reservacion guardada de forma exitosa. Total a pagar: {total} CUP. En menos de 24 horas le daremos respuestas de su sulicitud, los detalles y proceso a seguir')
            return render(request, 'crear_reservacion_especial_2.html',{'reservacion': reservacion })
        
    else: 
        
        form = Reservacion_PasadiaForm(request=request, pasadia = pasadia_id)
    contexto = {'pasadia': pasadia, 'form':form, 'pas':pas}     
    return render(request, 'pasadia.html', contexto)