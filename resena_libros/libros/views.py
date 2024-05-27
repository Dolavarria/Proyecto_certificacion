from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Libros, Autores, Generos, Reseñas,Contactos
from .forms import ReseñasModelForm, ContactosModelForm,LibrosModelForm,RegisterModelForm
# Create your views here.

#Permite registrar usuarios
def register(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)  # Utiliza tu formulario personalizado aquí
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterModelForm()  # Utiliza tu formulario personalizado aquí
    return render(request, 'register.html', {'form': form})

#Index, pagina de inicio
def indice(request):
    return render(request, 'index.html')

#Pagina que muestra los libros a usuarios luego de loguearse
@login_required
def home(request):
    libros = Libros.objects.all()
    return render(request, 'home.html', {'libros': libros})

#Formulario de contacto
def contacto(request):
    if request.method=='POST':
        form=ContactosModelForm(request.POST)
        if form.is_valid():
            Contactos.objects.create(**form.cleaned_data)  # Utiliza tu modelo Contacto aquí
            return HttpResponseRedirect('/contacto/exito/')
    else:
        form=ContactosModelForm()
    return render(request, 'contacto.html', {'form': form})
#Pagina de exito al lograr enviar el formulario de contacto
def contacto_exito(request):
    return render(request, 'contactoexito.html', {})


@staff_member_required
def libro_nuevo(request):
    if request.method=='POST':
        form=LibrosModelForm(request.POST)
        if form.is_valid():
            flan=form.save()
            return HttpResponseRedirect('/libro/nuevo/') 
    else:
        form=LibrosModelForm()
    return render(request, 'libro_nuevo.html', {'form': form})