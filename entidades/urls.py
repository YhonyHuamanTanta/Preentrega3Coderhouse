from django.contrib import admin
from django.urls import path, include
from entidades.views import *
from . import views
#from django.contrib.auth import logautView
#from django.contrib.auth import views as auth_views

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
    
    path('usuariosRegistrados/', usuariosRegistrados, name='usuariosRegistrados'),
    path('registrarUsuario/', registrarUsuario, name='registrarUsuario'),
    path('usuarios/eliminar/<int:id_usuario>/', eliminarUsuario, name='eliminarUsuario'),
    
    path('login/', iniciarSecion, name="login"),
    path('cerrarsesion/', cerrarSesion, name='cerrarsesion'),
    #path('logaut/', logautView.as_view(template_name= "entidades/logaut.html"), name="logaut"), 
    path('registrar/', registrarUsuarios, name="registrar"),
    path('cambiarContraseña/', cambiarContraseña, name='cambiarContraseña'),
    
    path('verViajesClientes/', verViajesClientes, name = "verViajesClientes"),    
    path('atenderClinetesForm/', atenderClinetesForm, name = "atenderClinetesForm"),
    path('atenderClinetesDelete/<id_atenderclinetes>', atenderClinetesDelete, name = "atenderClinetesDelete"),
    path('atenderClineteDelete/<id_atenderclinetes>', atenderClineteDelete, name = "atenderClineteDelete"),

]