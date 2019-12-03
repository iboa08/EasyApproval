from django.db import models

class Instructor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    institucion = models.CharField(max_length=40)
    cv = models.FileField()

class Curso(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    duracion = models.DurationField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    financiamiento = models.FloatField()
    costo = models.FloatField()
    aula = models.CharField(max_length=20)
    cupo = models.SmallIntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    institucion = models.CharField(max_length=40)
    cursos = models.ManyToManyField(Curso)
