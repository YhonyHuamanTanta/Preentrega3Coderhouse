from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User
# Create your models here.
class Buses(models.Model):
    nombre = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)

    class Meta:
        ordering = ["placa"]

    def __str__(self):
        return f"{self.nombre}, {self.placa}"

class Clientes(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.dni}, {self.apellido}, {self.nombre}"    

class Conductores(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"
        ordering = ["nombre", "apellido"]

    def __str__(self):
        return f"{self.dni}, {self.apellido}, {self.nombre}, {self.profesion}"

class Entregables(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    desde = models.CharField(max_length=80)
    lugar = models.CharField(max_length=80)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.dni}, {self.apellido}, {self.nombre}"
    
class AtenderClinetes(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    desde = models.CharField(max_length=80)
    llegada = models.CharField(max_length=80)
    nAsiento = models.CharField(max_length=80)
    costo = models.CharField(max_length=7)    
    
    def __str__(self):
        return f"{self.dni}, {self.apellido}, {self.nombre}"
    

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=500, blank=True)
    sitioWeb = models.URLField(blank=True)
    
    def __str__(self):
        return self.usuario.username
    """
@receiver(post_save, sender=User)
def crearUsuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
        
@receiver(post_save, sender=User)
def guardarUsuario(sender, instance, **kwargs):
    instance.usuario.save()
    
"""


   
#class Registrar(models.Model):
    #nombre = models.CharField(max_length=50)
    #apellido = models.CharField(max_length=60)
    #email = models.EmailField(required=True)
    #password1 = models.CharField(label="contraseña", widget=models.PasswordInput)
    #password2 = models.CharField(label="contraseña a confirmar", widget=models.PasswordInput)
    
    #def __str__(self):
        #return f"{self.nombre}, {self.apellido}, {self.email}"
        

    
    
#class Avatar(models.Model):   
    #imagen = models.ImageField(upload_to="avatares") 
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
        #return f"{self.user} {self.imagen}"   