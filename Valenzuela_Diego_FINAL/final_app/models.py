from django.db import models

# Create your models here.
class instituciones(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class inscritos(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.IntegerField()
    fecha = models.DateField()
    institucion = models.ForeignKey(instituciones, on_delete=models.CASCADE, db_column='idInstitucion')
    hora = models.TimeField()
    observacion = models.TextField()
    estado = models.CharField(max_length=25)
    