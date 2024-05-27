from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import password_validation  # Agrega esta línea

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
        fields = ['calificacion', 'comentario']
        widgets = {
            'calificacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Calificación (1-5)'
            }),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí'
            })
        }
        
class LibrosModelForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'descripcion', 'ano_publicacion', 'portada_url', 'genero', 'autor']
        labels = {
            'ano_publicacion': 'Año de publicación',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de libro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'ano_publicacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de publicación'}),
            'portada_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Inserte URL de imagen de la portada'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }

class RegisterModelForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'autocomplete': 'new-password'}),
    )
    class Meta:
        model = User 
        fields = ("username", "password1", "password2")
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
)
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
    )