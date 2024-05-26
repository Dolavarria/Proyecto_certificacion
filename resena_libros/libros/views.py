from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .models import Libros, Autores, Generos, Reseñas
from .forms import ReseñasForm, ContactosForm
# Create your views here.

def contacto(request):
    if request.method=='POST':
        #Crear instancia del formulario con los datos del request
        form=ContactosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contacto/exito/')
    else:
        form=ContactosForm()
    return render(request, 'contacto.html', {'form': form})

def contacto_exito(request):
    return render(request, 'contactoexito.html', {})