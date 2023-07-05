from importlib import import_module
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from hotel.forms import HotelForm, ContactoForm
from .models import Hotel, Oferta
from django.core.paginator import Paginator
from datetime import date
from django.core.mail import send_mail
from copy import deepcopy
from django.contrib import messages
from reservacion.forms import CarroAñadirProductoForm
from reservacion_especial.models import Oferta_Especial
from pasadía.models import Pasadia




# Create your views here.


def lista_hoteles( request):
    if request.method=='POST':
        form  =   HotelForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data     
            hoteles= Hotel.objects.all().filter(activo=True)
            if datos['cadena']:
                hoteles=hoteles.filter(cadena__nombre__icontains=datos['cadena'])
            if datos['nombre']:
                hoteles = hoteles.filter(nombre__icontains=datos['nombre'])
            if datos['polo']:
                hoteles = hoteles.filter(polo__icontains=datos['polo'])
            if datos['categoria']:
                hoteles = hoteles.filter(categoria=(datos['categoria']))
            if datos['transporte']:
                hoteles=hoteles.filter(transporte=datos['transporte'])
            if datos['ubicacion']:
                hoteles=hoteles.filter(ubicacion__icontains=datos['ubicacion'])
    else: 
        hoteles= Hotel.objects.all().filter(activo=True).order_by('categoria')
        form = HotelForm()
    pasadia = Pasadia.objects.all().exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())   
    oferta_especial = Oferta_Especial.objects.all().exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())
    hotel_id = 0
    for oferta_e in oferta_especial:
        hotel_id = oferta_e.hotel.id
    hotel_especial = Hotel.objects.all().filter(id = hotel_id)    
    paginator = Paginator(hoteles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contexto = {'hoteles': hoteles, 'page_obj': page_obj, 'form':form, 'oferta_especial': oferta_especial, 'hotel_especial' : hotel_especial,'pasadia':pasadia}
        
    return render(request, 'index.html', contexto)
    
    



def contactar(request):
    if request.method=='POST':
        form = ContactoForm( request.POST)
        if form.is_valid():
            print('es valido')
            form.save() 
            messages.success(request,'Su mensaje ha sido enviado de forma exitosa')
        else:
            messages.success(request,'Su mensaje no se ha enviado') 
        
    else:
        form=ContactoForm()
    return render(request, 'contactar.html', {'form':form})


    

def hotel_oferta(request, hotel_id):
    
    hoteles=Hotel.objects.filter(id=hotel_id)
    ofertas=Oferta.objects.filter(hotel=hotel_id).exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())
    paginator = Paginator(ofertas, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contexto = {'oferta': ofertas, 'page_obj': page_obj,'hotel':hoteles}
    return render(request,'hotel.html', contexto)



def oferta(request, oferta_id):
    oferta= Oferta.objects.get(id=oferta_id)
    if request.method=='POST':
        form  =   CarroAñadirProductoForm(request.POST, request=request)
        if form.is_valid():  
            print('es valido')
                 
    else: 
        form = CarroAñadirProductoForm(request=request, oferta=oferta_id)
    contexto = {'oferta': oferta, 'form':form}      
    return render(request, 'oferta.html', contexto)
    
