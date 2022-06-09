from django.db import models

# Create your models here.
class Tutorx(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Ocupacion = models.CharField(max_length=50)
    Edad = models.IntegerField()
    nombre_mascota = models.CharField(max_length=50)

def _str_(self) -> str:
    return self.Nombre+""+str(self.Tutorx)

class Mascota(models.Model):
    Nombre = models.CharField(max_length=50)
    Nombre_tutorx = models.CharField(max_length=50)
    Especie = models.CharField(max_length=50)
    Raza = models.CharField(max_length=50)
    Vacunas = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Peso = models.IntegerField()

class atencionprofesional(models.Model):
     Nombre_profesional= models.CharField(max_length=50)
     Motivo_de_atencion = models.CharField(max_length=200)
     Proxima_visita = models.DateField()