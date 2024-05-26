from django import forms
from .models import Contactos,Reseñas

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'email', 'mensaje']
        
class ReseñasForm(forms.ModelForm):
    class Meta:
        model = Reseñas
        fields = ['libro', 'calificacion', 'comentario']