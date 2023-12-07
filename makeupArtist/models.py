# makeupArtist/models.py

from django.db import models
from datetime import timedelta

class CategoriaServicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    categoria = models.ForeignKey(CategoriaServicio, related_name='servicios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.DurationField(default=timedelta(minutes=30))  # Esto está correcto


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    cliente = models.CharField(max_length=100)
    email = models.EmailField()
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Cita para {self.cliente} el {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    comentarios = models.TextField()

    def __str__(self):
        return self.nombre
