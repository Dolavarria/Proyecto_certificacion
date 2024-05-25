from django.db import models

# Create your models here.

class Contactos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mensaje=models.TextField()

class Generos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    
class Autores(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    