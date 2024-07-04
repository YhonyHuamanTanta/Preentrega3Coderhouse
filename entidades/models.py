from django.db import models

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