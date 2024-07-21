from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

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
            
class RegistrarForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

