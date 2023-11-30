from django.db import models

# Create your models here.
class Reservas(models.Model):
    nombre = models.CharField(max_length=80)
    telefono = models.IntegerField()
    email = models.EmailField()
    fechaReserva = models.DateField()
    hora = models.TimeField()
    NumPersonas = models.IntegerField()
    estado = models.CharField(max_length=15)
    observacion = models.CharField(max_length=150)
