# Generated by Django 5.0.6 on 2024-05-26 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_user_autores_seguidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='es_admin',
        ),
    ]
