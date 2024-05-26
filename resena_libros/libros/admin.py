from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
from .models import Contactos, Generos, Autores, Libros, User, Reseñas

admin.site.register(Contactos)
admin.site.register(Generos)
admin.site.register(Autores)
admin.site.register(Libros)
admin.site.register(User, UserAdmin)
admin.site.register(Reseñas)