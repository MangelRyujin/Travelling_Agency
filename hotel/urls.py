from cmath import phase
from hotel.views import  lista_hoteles, contactar
from django.urls import path



app_name='hotel'

urlpatterns = [
    path('', lista_hoteles , name='index'),
       
]
