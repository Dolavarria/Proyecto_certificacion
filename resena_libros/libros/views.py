from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Libros, Autores, Generos, Reseñas
from .forms import ReseñasForm, ContactosForm
# Create your views here.
