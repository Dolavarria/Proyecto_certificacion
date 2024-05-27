from django.core.management.base import BaseCommand
from libros.models import User

class Command(BaseCommand):
    help = 'Crea usuarios iniciales'

    def handle(self, *args, **options):
        # Crear usuario administrador
        admin_user, created = User.objects.get_or_create(username='administrador', email='administrador@mail.com')
        if created:
            admin_user.set_password('Abc123#')
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.save()

        # Crear usuario lector
        lector_user, created = User.objects.get_or_create(username='lector', email='lector@mail.com')
        if created:
            lector_user.set_password('Abc123#')
            lector_user.save()

        self.stdout.write(self.style.SUCCESS('Usuarios creados exitosamente'))