from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q,Avg
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from .models import Libros, Autores, Generos, Reseñas,Contactos
from .forms import ReseñasModelForm, ContactosModelForm,LibrosModelForm,RegisterModelForm,CustomAuthenticationForm
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

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

#Index, pagina de inicio
def indice(request):
    return render(request, 'index.html')

#Pagina que muestra los libros a usuarios luego de loguearse
def home(request):
    libros = Libros.objects.all()
    return render(request, 'home.html', {'libros': libros})

@login_required
def libro_detalle(request):
    generos = Generos.objects.all()
    autores = Autores.objects.all()
    libros = Libros.objects.all().annotate(calificacion_promedio=Avg('reseñas__calificacion'))

    query = request.GET.get('q')
    genero = request.GET.get('genero')
    autor = request.GET.get('autor')
    calificacion_min = request.GET.get('calificacion_min')
    calificacion_max = request.GET.get('calificacion_max')

    if query:
        libros = libros.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query)
        )
    if genero:
        libros = libros.filter(genero__nombre=genero)
    if autor:
        libros = libros.filter(autor__nombre=autor)
    if calificacion_min and calificacion_max:
        libros = libros.filter(calificacion_promedio__gte=calificacion_min, calificacion_promedio__lte=calificacion_max)

    return render(request, 'libro.html', {'libros': libros, 'generos': generos, 'autores': autores})

@login_required
def resenas(request, libro_id):
    libro = Libros.objects.get(id=libro_id)
    print(libro.id)  # Imprime el ID del libro en la consola
    if request.method == 'POST':
        form = ReseñasModelForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.libro = libro
            resena.usuario = request.user
            resena.save()
            return redirect('resenas', libro_id=libro.id)
        else:
            print(form.errors)
    else:
        form = ReseñasModelForm()
    resenas = Reseñas.objects.filter(libro=libro)
    return render(request, 'resenas.html', {'libro': libro, 'resenas': resenas, 'form': form})
@login_required
def mis_resenas(request):
    resenas = Reseñas.objects.filter(usuario=request.user)
    return render(request, 'mis_resenas.html', {'resenas': resenas})



def autor(request, autor_id):
    autor = get_object_or_404(Autores, id=autor_id)
    libros = Libros.objects.filter(autor=autor)
    return render(request, 'autor.html', {'autor': autor, 'libros': libros})

@login_required
def seguir_autor(request, autor_id):
    autor = get_object_or_404(Autores, pk=autor_id)
    request.user.autores_seguidos.add(autor)
    return redirect('autor', autor_id=autor_id)
@login_required
def dejar_seguir_autor(request, autor_id):
    autor = get_object_or_404(Autores, pk=autor_id)
    request.user.autores_seguidos.remove(autor)
    return redirect('autor', autor_id=autor_id)
@login_required
def autores_seguidos(request):
    autores = request.user.autores_seguidos.all()
    return render(request, 'autores_seguidos.html', {'autores': autores})
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