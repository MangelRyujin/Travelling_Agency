from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from turtle import mode
from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator
from datetime import datetime
from decimal import Decimal
from django import forms
from .models import *
from django.forms import ModelForm,TextInput,DateInput,CheckboxInput,NumberInput,EmailInput,ChoiceField,Select
from django.contrib import messages

# class OfertaForm(forms.Form):
    
#     adultos= forms.IntegerField(label= 'Cantidad de adultos',min_value=0,required= True,  widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de adultos", 'name':'adultos', 'type':'number'}) )
#     ninnos=forms.IntegerField(label= 'Cantidad de niños', min_value=0,required= True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de niños", 'name':'ninnos', 'type':'number'}) )
#     cantidad_de_habitaciones= forms.IntegerField(label= 'Cantidad de habitaciones', min_value=1,required= True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de habitaciones", 'name':'habitaciones', 'type':'number'}) )
# class ReservacionForm(forms.ModelForm):
#     class Meta:
#         model= Reservacion_Especial
#         fields = {'nombre_solicitante',
#                   'apellido1_solicitante',
#                   'apellido2_solicitante',
#                   'fecha_inicial',
#                   'fecha_final',
#                   'carnet',
#                   'transporte',
#                   'email',
#                   'telefono',
#                  }
#         widgets={
#             'nombre_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Nombre del solicitante", 'name':'nombre del solicitante' }),
#             'apellido1_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Primer apellido", 'name':'primer apellido' }),
#             'apellido2_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Segundo apellido", 'name':'segundo apellido' }),
#             'fecha_inicial':DateInput(attrs={'class':'form-control', 'type':'date','placeholder':"Fecha inicial", 'name':'fecha inicial' }),
#             'fecha_final':DateInput(attrs={'class':'form-control', 'type':'date','placeholder':"Fecha final", 'name':'fecha final' }),
#             'carnet': TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Carnet de identidad", 'name':'carnet de identidad' }),
#             'transporte':CheckboxInput(attrs={'class':'form-check-input ','placeholder':"Solicitar transporte", 'name':'solicitar transporte' }),
#             'email': EmailInput(attrs={'class':'form-control', 'type':'email','placeholder':'Email','name':'email'}),
#             'telefono':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Número de teléfono", 'name':'número de teléfono' }),    
#         }
class Reservacion_EspecialForm(forms.ModelForm):
    class Meta:
        model= Reservacion_Especial
        fields = {'nombre_solicitante',
                  'apellido1_solicitante',
                  'apellido2_solicitante',
                  'carnet',
                  'email',
                  'telefono',
                  'cantidad_habitaciones',
                  'adultos',
                  'ninnos',
                  'oferta_especial',
                  
                  
                 }
        
        widgets={
            
            'nombre_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Nombre del solicitante", 'name':'nombre del solicitante' }),
            'apellido1_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Primer apellido", 'name':'primer apellido' }),
            'apellido2_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Segundo apellido", 'name':'segundo apellido' }),
            'carnet': TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Carnet de identidad", 'name':'carnet de identidad' }),
            'email': EmailInput(attrs={'class':'form-control', 'type':'email','placeholder':'Email','name':'email'}),
            'telefono':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Número de teléfono", 'name':'número de teléfono' }),    
            'cantidad_habitaciones':NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de habitaciones", 'name':'habitaciones', 'type':'number'}),
            'ninnos':forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de niños", 'name':'ninnos', 'type':'number'}) ,
            'adultos':NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de adultos", 'name':'adultos', 'type':'number'}),
            'oferta_especial':Select(attrs={'class':'form-select','placeholder':"Oferta especial", 'name':'oferta especial'})
        }
        
    def __init__(self,*args,**kwargs):
            self.request = kwargs.pop("request")
            self.oferta = kwargs.pop("oferta")
            super(Reservacion_EspecialForm,self).__init__(*args,**kwargs)
 
    def clean(self, *args, **kwargs):
            cleaned_data = super(Reservacion_EspecialForm, self).clean(*args, **kwargs)
            ofertas = Oferta.objects.all().filter( id = self.oferta)
            adultos = self.cleaned_data.get('adultos')
            ninnos = self.cleaned_data.get('ninnos')
            cantidad_habitaciones = self.cleaned_data.get('cantidad_habitaciones')
            ofert_especial = self.cleaned_data.get('oferta_especial')
            ofertas_especiales = Oferta_Especial.objects.all().exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())
            max_a = 0
            min_a = 0
            max_n = 0
            min_n = 0
            for of in ofertas_especiales:
                if of != ofert_especial:
                    messages.success(self.request,f'Debe de escoger la oferta especial {of.nombre}')
                    raise forms.ValidationError('Seleccione correctamente la oferta especial correcta')
            for o in ofertas:
                max_a = o.cant_max_adulto*cantidad_habitaciones
                min_a = o.cant_min_adulto*cantidad_habitaciones
                max_n = o.cant_max_ninnos*cantidad_habitaciones
                min_n = o.cant_min_ninnos*cantidad_habitaciones
            if adultos > max_a or adultos < min_a:
                messages.success(self.request,f'La cantidad de niños o adultos es incorrecta')
                raise forms.ValidationError('La cantidad de adultos es incorrecta')
            if ninnos > max_n or ninnos < min_n:
                messages.success(self.request,f'La cantidad de niños o adultos es incorrecta')
                raise forms.ValidationError('La cantidad de niños es incorrecta')  
            for ofer in ofertas_especiales:
                if ofer.Total_de_personas_en_el_viaje() + (adultos+ninnos)  > ofer.total_de_personas :
                    if ofer.total_de_personas - ofer.Total_de_personas_en_el_viaje() == 0:
                        messages.success(self.request,f'Lo sentimos la capacidad del viaje está completa')
                        raise forms.ValidationError('La capacidad del viaje está completa')
                    else:
                        total = ofer.total_de_personas - ofer.Total_de_personas_en_el_viaje()
                        messages.success(self.request,f'Lo sentimos la capacidad de personas que puede reservar es de {total}')
                        raise forms.ValidationError('No puede reservar más')
            
            
            return cleaned_data