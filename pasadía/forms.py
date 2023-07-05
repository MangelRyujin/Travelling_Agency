from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import *
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm,TextInput,DateInput,CheckboxInput,NumberInput,EmailInput,BooleanField,Select
from django.contrib import messages

class Reservacion_PasadiaForm(forms.ModelForm):
    class Meta:
        model= Reservacion_Pasadia
        fields = {'nombre_solicitante',
                  'apellido1_solicitante',
                  'apellido2_solicitante',
                  'carnet',
                  'email',
                  'telefono',
                  'adultos',
                  'ninnos',
                  'pasadia',
                  
                  
                 }
        
        widgets={
            
            'nombre_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Nombre del solicitante", 'name':'nombre del solicitante' }),
            'apellido1_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Primer apellido", 'name':'primer apellido' }),
            'apellido2_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Segundo apellido", 'name':'segundo apellido' }),
            'carnet': TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Carnet de identidad", 'name':'carnet de identidad' }),
            'email': EmailInput(attrs={'class':'form-control', 'type':'email','placeholder':'Email','name':'email'}),
            'telefono':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Número de teléfono", 'name':'número de teléfono' }),    
            'ninnos':forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de niños", 'name':'ninnos', 'type':'number'}) ,
            'adultos':NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de adultos", 'name':'adultos', 'type':'number'}),
            'pasadia':Select(attrs={'class':'form-select','placeholder':"Oferta especial", 'name':'oferta especial'})
        }
        
    def __init__(self,*args,**kwargs):
            self.request = kwargs.pop("request")
            self.pasadia = kwargs.pop("pasadia")
            super(Reservacion_PasadiaForm,self).__init__(*args,**kwargs)
 
    def clean(self, *args, **kwargs):
            cleaned_data = super(Reservacion_PasadiaForm, self).clean(*args, **kwargs)
            
            adultos = self.cleaned_data.get('adultos')
            ninnos = self.cleaned_data.get('ninnos')
            pasadia_clean = self.cleaned_data.get('pasadia')
            pasadia = Pasadia.objects.all().exclude(fecha_inicial_vigente__gte=date.today()).exclude(fecha_final_vigente__lte=date.today())
            for p in pasadia:
                
                if pasadia_clean.id == p.id :
                    
                    for of in pasadia:
                        if of != pasadia_clean:
                            messages.success(self.request,f'Debe de escoger el pasadia {of.nombre}')
                            raise forms.ValidationError('Seleccione correctamente el nombre del pasadia correcto')
          
                    for ofer in pasadia:
                        if ofer.Total_de_personas_en_el_viaje() + (adultos+ninnos)  > ofer.total_de_personas :
                            if ofer.total_de_personas - ofer.Total_de_personas_en_el_viaje() == 0:
                                messages.success(self.request,f'Lo sentimos la capacidad del viaje está completa')
                                raise forms.ValidationError('La capacidad del viaje está completa')
                            else:
                                total = ofer.total_de_personas - ofer.Total_de_personas_en_el_viaje()
                                messages.success(self.request,f'Lo sentimos la capacidad de personas que puede reservar es de {total}')
                                raise forms.ValidationError('No puede reservar más')
            
                else:
                    messages.success(self.request,f'La oferta pasadia que tiene que seleccionar es: {p.nombre}')
                    raise forms.ValidationError('Escoja la oferta pasadia correcta')
            
            return cleaned_data