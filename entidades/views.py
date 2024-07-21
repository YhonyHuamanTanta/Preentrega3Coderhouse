from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'entidades/index.html')

def inicio(request):
    return render(request, 'entidades/inicio.html')

@login_required
def buses(request):
    contexto = {"buses": Buses.objects.all()}
    return render(request, 'entidades/buses.html', contexto)

@login_required
def busesForm(request):
    if request.method == "POST":
        miForm = BusesForm(request.POST)
        if miForm.is_valid():
            buses_nombre = miForm.cleaned_data.get("nombre")
            buses_placa = miForm.cleaned_data.get("placa")
            buses = Buses(nombre=buses_nombre, placa=buses_placa)
            buses.save()
            contexto = {"buses": Buses.objects.all() }
            return render(request, "entidades/buses.html", contexto)
    else:
        miForm = BusesForm()
    
    return render(request, "entidades/busesRegistrarForm.html", {"form": miForm})

@login_required
def busesUpdate(request, id_buses):
    buses = Buses.objects.get(id=id_buses)
    if request.method == "POST":
        miForm = BusesForm(request.POST)
        if miForm.is_valid():
            buses.nombre = miForm.cleaned_data.get("nombre")
            buses.placa = miForm.cleaned_data.get("placa")
            buses.save()
            contexto = {"buses": Buses.objects.all() }
            return render(request, "entidades/buses.html", contexto)       
    else:
        miForm = BusesForm(initial={"nombre": buses.nombre, "placa": buses.placa}) 
    
    return render(request, "entidades/busesForm.html", {"form": miForm})

@login_required
def busesDelete(request, id_buses):
    buses = Buses.objects.get(id=id_buses)
    buses.delete()
    contexto = {"buses": Buses.objects.all() }
    return render(request, "entidades/buses.html", contexto)  


@login_required
def conductores(request):
    contexto = {"conductores": Conductores.objects.all()}
    return render(request, 'entidades/conductores.html', contexto)

@login_required
def conductoresForm(request):
    if request.method == "POST":
        miForm = ConductoresForm(request.POST)
        if miForm.is_valid():
            conductores_dni = miForm.cleaned_data.get("dni")
            conductores_nombre = miForm.cleaned_data.get("nombre")
            conductores_apellido = miForm.cleaned_data.get("apellido")
            conductores_email = miForm.cleaned_data.get("email")
            conductores_profesion = miForm.cleaned_data.get("profesion")
            conductores = Conductores(dni=conductores_dni, nombre=conductores_nombre, apellido=conductores_apellido, email=conductores_email, profesion=conductores_profesion)
            conductores.save()
            contexto = {"conductores": Conductores.objects.all() }
            return render(request, "entidades/conductores.html", contexto)
    else:
        miForm = ConductoresForm()
    
    return render(request, "entidades/conductoresRegistrarForm.html", {"form": miForm})

@login_required
def conductoresUpdate(request, id_conductores):
    conductores = Conductores.objects.get(id=id_conductores)
    if request.method == "POST":
        miForm = ConductoresForm(request.POST)
        if miForm.is_valid():
            conductores.dni = miForm.cleaned_data.get("dni")
            conductores.nombre = miForm.cleaned_data.get("nombre")
            conductores.apellido = miForm.cleaned_data.get("apellido")
            conductores.profesion = miForm.cleaned_data.get("profesion")
            conductores.email = miForm.cleaned_data.get("email")
            conductores.save()
            contexto = {"conductores": Conductores.objects.all() }
            return render(request, "entidades/conductores.html", contexto)
    else:
        miForm = ConductoresForm(initial={"dni": conductores.dni, "nombre": conductores.nombre, "apellido": conductores.apellido, "profesion":conductores.profesion, "email": conductores.email})
    
    return render(request, "entidades/conductoresForm.html", {"form": miForm})
    
    
@login_required
def conductoresDelete(request, id_conductores):
    conductores = Conductores.objects.get(id=id_conductores)
    conductores.delete()
    contexto = {"conductores": Conductores.objects.all() }
    return render(request, "entidades/conductores.html", contexto)

@login_required
def clientes(request):
    contexto = {"clientes": Clientes.objects.all()}
    return render(request, 'entidades/clientes.html', contexto)

@login_required
def clientesForm(request):
    if request.method == "POST":
        miForm = ClientesForm(request.POST)
        if miForm.is_valid():
            clientes_dni = miForm.cleaned_data.get("dni")
            clientes_nombre = miForm.cleaned_data.get("nombre")
            clientes_apellido = miForm.cleaned_data.get("apellido")
            clientes_email = miForm.cleaned_data.get("email")
            clientes = Clientes(dni=clientes_dni, nombre=clientes_nombre, apellido=clientes_apellido, email=clientes_email)
            clientes.save()
            contexto = {"clientes": Clientes.objects.all() }
            return render(request, "entidades/clientes.html", contexto)
    else:
        miForm = ClientesForm()
    
    return render(request, "entidades/clientesRegistrarForm.html", {"form": miForm})

@login_required
def clientesUpdate(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    if request.method == "POST":
        miForm = ClientesForm(request.POST)
        if miForm.is_valid():
            clientes.dni = miForm.cleaned_data.get("dni")
            clientes.nombre = miForm.cleaned_data.get("nombre")
            clientes.apellido = miForm.cleaned_data.get("apellido")
            clientes.email = miForm.cleaned_data.get("email")
            clientes.save()
            contexto = {"clientes": Clientes.objects.all() }
            return render(request, "entidades/clientes.html", contexto)
    else:
        miForm = ClientesForm(initial={"dni": clientes.dni, "nombre": clientes.nombre, "apellido": clientes.apellido, "email": clientes.email})
    
    return render(request, "entidades/clientesForm.html", {"form": miForm})

@login_required
def clientesDelete(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    clientes.delete()
    contexto = {"clientes": Clientes.objects.all() }
    return render(request, "entidades/clientes.html", contexto) 

@login_required
def entregables(request):
    contexto = {"entregables": Entregables.objects.all()}
    return render(request, 'entidades/entregables.html', contexto)

@login_required
def entregablesForm(request):
    if request.method == "POST":
        miForm = EntregablesForm(request.POST)
        if miForm.is_valid():
            entregables_dni = miForm.cleaned_data.get("dni")
            entregables_nombre = miForm.cleaned_data.get("nombre")
            entregables_apellido = miForm.cleaned_data.get("apellido")
            entregables_desde = miForm.cleaned_data.get("desde")
            entregables_lugar = miForm.cleaned_data.get("lugar")
            entregables_fechaEntrega= miForm.cleaned_data.get("fechaEntrega")
            entregables_entregado = miForm.cleaned_data.get("entregado")
            entregables = Entregables(dni=entregables_dni, nombre=entregables_nombre, apellido=entregables_apellido, desde= entregables_desde, lugar=entregables_lugar , fechaEntrega=entregables_fechaEntrega, entregado=entregables_entregado)
            entregables.save()
            contexto = {"entregables": Entregables.objects.all() }
            return render(request, "entidades/entregables.html", contexto)
    else:
        miForm = EntregablesForm()
    
    return render(request, "entidades/entregablesRegistrarForm.html", {"form": miForm})
    
@login_required
def entregablesUpdate(request, id_entregables ):
    entregables = Entregables.objects.get(id=id_entregables)
    if request.method == "POST":
        miForm = EntregablesForm(request.POST)
        if miForm.is_valid():
            entregables.dni = miForm.cleaned_data.get("dni")
            entregables.nombre = miForm.cleaned_data.get("nombre")
            entregables.apellido = miForm.cleaned_data.get("apellido")
            entregables.desde = miForm.cleaned_data.get("desde")
            entregables.lugar = miForm.cleaned_data.get("lugar")
            entregables.fechaEntrega= miForm.cleaned_data.get("fechaEntrega")
            entregables.entregado = miForm.cleaned_data.get("entregado")
            entregables.save()
            contexto = {"entregables": Entregables.objects.all() }
            return render(request, "entidades/entregables.html", contexto)
    else:
        miForm = EntregablesForm(initial={"dni":entregables.dni, "nombre":entregables.nombre, "apellido":entregables.apellido, "desde":entregables.desde, "lugar":entregables.lugar , "fechaEntrega":entregables.fechaEntrega, "entregado":entregables.entregado})
    
    return render(request, "entidades/entregablesForm.html", {"form": miForm})

@login_required
def entregablesDelete(request, id_entregables):
    entregables = Entregables.objects.get(id=id_entregables)
    entregables.delete()
    contexto = {"entregables": Entregables.objects.all() }
    return render(request, "entidades/entregables.html", contexto) 

@login_required
def buscarDni(request):
    return render(request, "entidades/buscar.html")

@login_required
def encontrarDni(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        dni = Entregables.objects.filter(dni__icontains=patron)
        contexto = {'entregables': dni}    
    else:
        contexto = {'entregables': Entregables.objects.all()}
        
    return render(request, "entidades/entregables.html", contexto)



def iniciarSecion(request):
    if request.method == "POST":
        
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
        
    else:
        messages.error(request, 'El nombre de usuario o contraseña incorrectos')
        miForm = AuthenticationForm()

    return render(request, "entidades/inicio.html", {"form": miForm})
"""
def iniciarSecion(request):
    if request.method =="GET":
        return render(request, "entidades/inicio.html", {"form": AuthenticationForm})
    else:
        user = authenticate( request, username=request.POST["username"], password=request.POST["password"],
            
        )
        if user is not None:
            return render(request, "entidades/inicio.html", {"form": AuthenticationForm, "error": "Datos incorrecto"}),
        else: 
            login(request,user)
            return redirect('home')
"""

def registrar(request):
    if request.method == "POST":
        miForm = RegistrarForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistrarForm()

    return render(request, "entidades/inicio.html", {"form": miForm}) 



def inicio(request):
    return render(request, 'entidades/inicio.html')



"""
def registrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registrar')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('registrar')
        
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)
        messages.success(request, 'Te has registrado correctamente.')
        return redirect('home')
    return render(request, 'entidades/inicio.html')

"""
@login_required
def cambiarContraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Tu contraseña ha sido actualizada exitosamente.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'entidades/cambiarcontraseña.html', {
        'form': form
    })
    
def cerrarSesion(request):
    logout(request)
    return redirect('login')


"""
def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/inicio.html", {"form": miForm})


def registrar(request):
    if request.method=="POST":
        miForm = RegistrarForm(request.POST)
        if miForm.is_valid:
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistrarForm()
    return request(request, "entidades/inicio.html", {"form": miForm})
"""

def registrarUsuarios(request):
    usuario = Usuario
    form = RegistrarForm
    if request.method=="POST":
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'entidades/index.html',{"form": form})

@login_required
def usuariosRegistrados(request):
    usuarios = User.objects.all()
    return render(request, 'entidades/usuariosRegistrados.html', {'usuarios': usuarios})

@login_required
def eliminarUsuario(request, id_usuario):
    usuario = get_object_or_404(User, id=id_usuario)
    if request.method == "POST":
        usuario.delete()
        return redirect('usuariosRegistrados')
    return render(request, 'entidades/usuariosRegistrados.html', {'usuario': usuario})

"""
def registrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario ha sido creado exitosamente.')
            return redirect('usuariosRegistrados')
    else:
        form = UserCreationForm()
    return render(request, 'entidades/registrarUsuariosForm.html', {'form': form})
"""



@login_required
def registrarUsuario(request):
    return render(request, 'entidades/registrarUsuariosBus.html')