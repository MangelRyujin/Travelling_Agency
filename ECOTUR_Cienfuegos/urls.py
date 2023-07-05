"""ECOTUR_Cienfuegos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cmath import phase
from operator import index
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hotel.views import  contactar, hotel_oferta, oferta
from reservacion.views import  *
from reservacion_especial.views import *
from pasadía.views import * 



urlpatterns = [
    path('sitio-administrativo-de-ECOTUR/', admin.site.urls),
    path('', include('hotel.urls',namespace='hotel')),
    path('contactar/', contactar, name='contactar'),
    path('hotel/<int:hotel_id>', hotel_oferta, name='hotel_oferta'),
    path('oferta/<int:oferta_id>', oferta, name='oferta'),
    path('carro/<int:oferta_id>/',agregar_oferta, name='carrito'),
    path('detalles/',carro_detalles, name='detalles'),
    path('remove/<int:oferta_id>/', carro_remove, name='carro_remove' ),
    path('crear_reservacion/', crear_Reservacion, name='reservacion'),
    path('limpiar/', carro_limpiar, name='carro_limpiar' ),
    path('hotel_oferta_especial/<int:hotel_id>', hotel_oferta_especial, name='hotel_oferta_especial'),
    path('oferta_especial/<int:oferta_id>', oferta_especial, name='oferta_especial'),
    path('reservacion_especial/<int:oferta_id>', reservacion_especial, name='reservacion_especial'),
    path('pasadia/<int:pasadia_id>', pasadia, name='pasadia'),
    
    
     
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) 






