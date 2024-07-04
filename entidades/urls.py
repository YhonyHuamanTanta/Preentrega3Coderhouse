from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name = "home"),
    
    path('inicio/', inicio, name = "inicio"),
    
    path('buses/', buses, name = "buses"),
    path('busesUpdate/<id_buses>/', busesUpdate, name="busesUpdate"),
    path('busesDelete/<id_buses>/', busesDelete, name="busesDelete"),
    path('busesForm/', busesForm, name="busesForm"),
    
    path('conductores/', conductores, name = "conductores"),
    path('conductoresForm/', conductoresForm, name = "conductoresForm"),
    path('conductoresUpdate/<id_conductores>/', conductoresUpdate, name="conductoresUpdate"),
    path('conductoresDelete/<id_conductores>/', conductoresDelete, name="conductoresDelete"),
    
    path('clientes/', clientes, name = "clientes"),
    path('clientesForm/', clientesForm, name="clientesForm"),
    path('clientesUpdate/<id_clientes>/', clientesUpdate, name="clientesUpdate"),
    path('clientesDelete/<id_clientes>/', clientesDelete, name="clientesDelete"),
    
    path('entregables/', entregables, name = "entregables"),
    path('entregablesForm/', entregablesForm, name = "entregablesForm"),
    path('entregablesUpdate/<id_entregables>', entregablesUpdate, name = "entregablesUpdate"),
    path('entregablesDelete/<id_entregables>', entregablesDelete, name = "entregablesDelete"),
 
    path('buscarDni/', buscarDni, name="buscarDni"),
    path('encontrarDni/', encontrarDni, name="encontrarDni"),
    
    
    
    
]