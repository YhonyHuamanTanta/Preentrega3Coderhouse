from django import forms 

class BusesForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Modelo del Bus")
    placa = forms.CharField(max_length=7)
    
class ConductoresForm(forms.Form):
    dni = forms.CharField(max_length=8)
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    profesion = forms.CharField(max_length=50)
    
class ClientesForm(forms.Form):
    dni = forms.CharField(max_length=8)
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

class EntregablesForm(forms.Form):
    dni = forms.CharField(max_length=8)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=60)
    desde = forms.CharField(max_length=80)
    lugar = forms.CharField(max_length=80)
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()