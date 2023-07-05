from tkinter import Widget
from django import forms
from django.forms import ModelForm
from hotel.models import *
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm,TextInput,DateInput,CheckboxInput,NumberInput,EmailInput,BooleanField



class HotelForm(forms.Form):
    
    polos= [('','Polo'),('occ','occidente'),('cen','centro'),('ori','orinete')]
    
    nombre = forms.CharField(label= 'Nombre del hotel', max_length=50, required= False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Nombre del hotel", 'name':'nombre'}) )
    cadena = forms.CharField(label='Cadena hotelera', required= False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Cadena hotelera', 'name':'cadena hotelera'}))
    categoria = forms.IntegerField(label= 'Estrellas', required=False, min_value=1, max_value=5, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Estrellas", 'name':'estrella'}))
    polo = forms.ChoiceField(label = 'Polo' ,required=False, choices=polos, widget=forms.Select(attrs={'class':'form-select','placeholder':"Polo", 'name':'polo'}))
    transporte = forms.BooleanField(label = 'Transporte', required=False, widget= forms.CheckboxInput(attrs={'type':'checkbox','placeholder':"Transporte", 'name':'transporte' }))
    ubicacion = forms.CharField(label= 'Provincia', max_length=50, required= False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Provincia", 'name':'provincia'}) )    
# class ContactarForm(forms.Form):
    
#     nombre =  forms.CharField(label= 'Nombre', max_length=50, required= False, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Nombre", 'name':'nombre' }) )   
#     email =  forms.CharField(label= 'Email', max_length=50, required= False, widget=forms.TextInput(attrs={'class':'form-control', 'type':'email','placeholder':"Email", 'name':'email'}) )
    
#     mensaje = forms.EmailField(label= 'Mensaje' ,required= False, widget= forms.Textarea(attrs={'class':'form-control', 'data-validation-required-message':'Please enter a message.','type':'text','placeholder':"Mensaje", 'name':'mensaje','style':'height: 150px;'}) )
#    #<textarea class="form-control" id="message" data-validation-required-message="Please enter a message." required="" placeholder="Mensaje" style="height: 150px;" name="Mensaje"></textarea> 

# class OfertaForm(forms.Form):
    
#     adultos= forms.IntegerField(label= 'Cantidad de adultos',min_value=0,required= True,  widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de adultos", 'name':'adultos', 'type':'number'}) )
#     ninnos=forms.IntegerField(label= 'Cantidad de niños', min_value=0,required= True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de niños", 'name':'ninnos', 'type':'number'}) )
    
    # def clean_adultos(self):
    #     print('adultos')
    #     errors= 'error'
    #     raise ValidationError(errors)
    
    # def clean(self):
    #     super().clean()
    #     errors= dict()
    #     raise ValidationError(errors)
    
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = {'nombre',
                  'email',
                  'mensaje'}
        widgets= {
            'nombre':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Nombre", 'name':'nombre' }),
            'email': EmailInput(attrs={'class':'form-control', 'type':'email','placeholder':'Email','name':'email'}),
            'mensaje': TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Mensaje", 'name':'mensaje' }),
        }
        