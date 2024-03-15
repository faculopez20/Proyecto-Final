from django.urls import path
from Inicio.views import  Usuario, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('usuarios/', Usuario , name='usuarios'),
    
    
  ]