from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contactos,Reseñas,Libros,User

class ContactosModelForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 5}),
        }
        
class ReseñasModelForm(forms.ModelForm):
    class Meta:
        model = Reseñas
        fields = ['libro', 'calificacion', 'comentario']
        
class LibrosModelForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'descripcion', 'ano_publicacion', 'portada_url', 'genero', 'autor']

class RegisterModelForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ("username", "email", "password1", "password2")  