# appJazmine/admin.py

from django.contrib import admin
from .models import CategoriaServicio, Servicio, Producto, Cita

admin.site.register(CategoriaServicio)
admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Cita)
