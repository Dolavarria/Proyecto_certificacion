from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Contactos(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mensaje=models.TextField()

class Generos(models.Model):
    nombre=models.CharField(max_length=50)
    
class Autores(models.Model):
    nombre=models.CharField(max_length=50)

class Libros(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField()	
    ano_publicacion=models.DateField()
    portada_url=models.URLField()
    genero=models.ForeignKey(Generos, on_delete=models.CASCADE)
    autor=models.ForeignKey(Autores, on_delete=models.CASCADE)
    
class User(AbstractUser):
    es_admin=models.BooleanField(default=False)
    autores_seguidos = models.ManyToManyField('Autores', related_name='seguidores')
    
class Reseñas(models.Model):
    libro=models.ForeignKey(Libros, on_delete=models.CASCADE)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario=models.TextField()
    fecha_resena=models.DateTimeField(auto_now_add=True)
    