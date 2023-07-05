from django import forms
from .models import Reservacion , Items_Reservacion
from .models import Oferta, Hotel
from django.forms import ModelForm,TextInput,DateInput,CheckboxInput,NumberInput,EmailInput
from .carro import Carro
from django.contrib import messages
from datetime import date

class CarroAñadirProductoForm(forms.Form):
    adultos= forms.IntegerField(label= 'Cantidad de adultos',required= True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de adultos", 'name':'adultos', 'type':'number'}) )
    ninnos=forms.IntegerField(label= 'Cantidad de niños',required= True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Cantidad de niños", 'name':'ninnos', 'type':'number'}) )

    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop("request")
        self.oferta = kwargs.pop("oferta")
        super(CarroAñadirProductoForm,self).__init__(*args,**kwargs)

    def clean_adultos(self):
        adultos = self.cleaned_data.get('adultos')
        items = Oferta.objects.all().filter( id = self.oferta)
        print(items)
        max = 0
        min = 0
        for item in items:
            max = item.cant_max_adulto
            min =  item.cant_min_adulto
            if adultos < item.cant_max_adulto or adultos > item.cant_min_adulto :
                messages.success(self.request,f'La cantidad de niños o adultos es incorrecta')
                raise forms.ValidationError('La cantidad de adultos es incorrecta')
        
        return adultos
    def clean_ninnos(self):
        ninnos = self.cleaned_data.get('ninnos')
        items = Oferta.objects.all().filter( id = self.oferta)
        max = 0
        min = 0
        for item in items:
            max = item.cant_max_ninnos
            min =  item.cant_min_ninnos
            if ninnos > item.cant_max_ninnos or ninnos < item.cant_min_ninnos:
                # if max == min:
                #     messages.success(self.request,f' La cantidad de adultos  a reservar tiene que ser de ')
                # else:
                messages.success(self.request,f' La cantidad de niños o adultos es incorrecta ')
                raise forms.ValidationError('La cantdad de niños es incorrecta')
        return ninnos


    
class ReservacionForm(forms.ModelForm):
    class Meta:
        model= Reservacion
        fields = {'nombre_solicitante',
                  'apellido1_solicitante',
                  'apellido2_solicitante',
                  'fecha_inicial',
                  'fecha_final',
                  'carnet',
                  'transporte',
                  'email',
                  'telefono',
                 }
        
        widgets={
            'nombre_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Nombre del solicitante", 'name':'nombre del solicitante' }),
            'apellido1_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Primer apellido", 'name':'primer apellido' }),
            'apellido2_solicitante':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Segundo apellido", 'name':'segundo apellido' }),
            'fecha_inicial':DateInput(attrs={'class':'form-control', 'type':'date','placeholder':"Fecha inicial", 'name':'fecha inicial' }),
            'fecha_final':DateInput(attrs={'class':'form-control', 'type':'date','placeholder':"Fecha final", 'name':'fecha final' }),
            'carnet': TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Carnet de identidad", 'name':'carnet de identidad' }),
            'transporte':CheckboxInput(attrs={'class':'form-check-input ','placeholder':"Solicitar transporte", 'name':'solicitar transporte' }),
            'email': EmailInput(attrs={'class':'form-control', 'type':'email','placeholder':'Email','name':'email'}),
            'telefono':TextInput(attrs={'class':'form-control', 'type':'text','placeholder':"Número de teléfono", 'name':'número de teléfono' }),    
        }
        
        
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop("request")
        super(ReservacionForm,self).__init__(*args,**kwargs)
    
    def clean(self, *args, **kwargs):
        cleaned_data = super(ReservacionForm, self).clean(*args, **kwargs)
        
        fecha_inicial = self.cleaned_data.get('fecha_inicial')
        
        fecha_final = self.cleaned_data.get('fecha_final')
        
        dias = 0
        items = Carro(self.request)
        inicial = self.cleaned_data.get('fecha_inicial')
        final = self.cleaned_data.get('fecha_final')
        fecha_inicial_limite = 0
        fecha_final_limite = 0 
        mayor = 0
        menor = 99999999999
        
        items = Carro(self.request)
        if fecha_inicial > fecha_final:
            messages.success(self.request,f'La fecha inicial es mayor a la final')
            raise forms.ValidationError(self.request, f'La fecha inicial debe de ser antes que la fecha final')
        else:
            for item in items:
                if mayor <= item['oferta'].fecha_inicial_reserva.toordinal():
                    mayor = item['oferta'].fecha_inicial_reserva.toordinal()
                    inicial = item['oferta'].fecha_inicial_reserva
                    fecha_inicial_limite = item['oferta'].fecha_inicial_reserva.toordinal()
                if menor >= item['oferta'].fecha_final_reserva.toordinal():
                    menor = item['oferta'].fecha_final_reserva.toordinal()
                    final = item['oferta'].fecha_final_reserva
                    fecha_final_limite = item['oferta'].fecha_final_reserva.toordinal()
            if fecha_final.toordinal() < fecha_inicial_limite or fecha_final.toordinal() > fecha_final_limite or fecha_inicial.toordinal() < fecha_inicial_limite or fecha_inicial.toordinal() > fecha_final_limite:    
                messages.success(self.request,f'La fecha de reservacion no se encuentra dentro del rango usted solo puede reservar desde {inicial} hasta {final}  ')
                raise forms.ValidationError('fecha inicial no se encuentra dentro del rango para reservar')  
            else:
                for item in items:
                    if dias < item['oferta'].dias_min:
                        dias = item['oferta'].dias_min
                if fecha_final.toordinal()-fecha_inicial.toordinal()+1 < dias:
                    messages.success(self.request,f'Usted debe reservar mínimo {dias} días')
                    raise forms.ValidationError(self.request, f'Debe reservar mínimo {dias} dias')     
        return cleaned_data