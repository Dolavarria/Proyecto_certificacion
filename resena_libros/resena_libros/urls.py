"""
URL configuration for resena_libros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from libros.views import indice,home,register,contacto_exito,libro_nuevo,contacto,libro_detalle,resenas,mis_resenas,autor,seguir_autor,dejar_seguir_autor,autores_seguidos,CustomLoginView

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',indice,name="indice"),
    path('home/',home,name="home"),
    path('register/', register, name='register'),
    path('contacto/',contacto,name="contacto"),
    path('contacto/exito/',contacto_exito, name="contacto_success"), 
    path('libro/nuevo/',libro_nuevo,name='libro_nuevo'),
    path('libro/', libro_detalle, name='libro'),
    path('libro/<int:libro_id>/resenas', resenas, name='resenas'),
    path('mis_resenas/', mis_resenas, name='mis_resenas'),
    path('autor/<int:autor_id>/', autor, name='autor'),
    path('autor/<int:autor_id>/seguir', seguir_autor, name='seguir_autor'),
    path('autor/<int:autor_id>/dejar_seguir', dejar_seguir_autor, name='dejar_seguir_autor'),
    path('autores_seguidos', autores_seguidos, name='autores_seguidos'),


   
]
