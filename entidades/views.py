from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'entidades/index.html')

def inicio(request):
    return render(request, 'entidades/inicio.html')

def buses(request):
    contexto = {"buses": Buses.objects.all()}
    return render(request, 'entidades/buses.html', contexto)

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
    
    return render(request, "entidades/busesForm.html", {"form": miForm})

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

def busesDelete(request, id_buses):
    buses = Buses.objects.get(id=id_buses)
    buses.delete()
    contexto = {"buses": Buses.objects.all() }
    return render(request, "entidades/buses.html", contexto)  



def conductores(request):
    contexto = {"conductores": Conductores.objects.all()}
    return render(request, 'entidades/conductores.html', contexto)

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
    
    return render(request, "entidades/conductoresForm.html", {"form": miForm})

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
    
    

def conductoresDelete(request, id_conductores):
    conductores = Conductores.objects.get(id=id_conductores)
    conductores.delete()
    contexto = {"conductores": Conductores.objects.all() }
    return render(request, "entidades/conductores.html", contexto)


def clientes(request):
    contexto = {"clientes": Clientes.objects.all()}
    return render(request, 'entidades/clientes.html', contexto)

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
    
    return render(request, "entidades/clientesForm.html", {"form": miForm})

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

def clientesDelete(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    clientes.delete()
    contexto = {"clientes": Clientes.objects.all() }
    return render(request, "entidades/clientes.html", contexto) 


def entregables(request):
    contexto = {"entregables": Entregables.objects.all()}
    return render(request, 'entidades/entregables.html', contexto)

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
    
    return render(request, "entidades/entregablesForm.html", {"form": miForm})
    
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

def entregablesDelete(request, id_entregables):
    entregables = Entregables.objects.get(id=id_entregables)
    entregables.delete()
    contexto = {"entregables": Entregables.objects.all() }
    return render(request, "entidades/entregables.html", contexto) 


def buscarDni(request):
    return render(request, "entidades/buscar.html")

def encontrarDni(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        dni = Clientes.objects.filter(dni__icontains=patron)
        contexto = {'clientes': dni}    
    else:
        contexto = {'clientes': Clientes.objects.all()}
        
    return render(request, "entidades/clientes.html", contexto)