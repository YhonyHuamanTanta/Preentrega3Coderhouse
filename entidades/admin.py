from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Buses)
admin.site.register(Clientes)
admin.site.register(Conductores)
admin.site.register(Entregables)