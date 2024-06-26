# Titulo del proyecto

Plataforma de Reseñas de Libros

## Descripción del proyecto
Desarrollar un sitio web dinámico y responsivo que facilite la gestión de reseñas de libros,
permitiendo a los usuarios escribir reseñas, calificar libros y seguir a autores. Esta
plataforma ofrecerá una experiencia de usuario fluida y adaptable en diversos dispositivos,
garantizando que los usuarios puedan interactuar de manera intuitiva y accesible.
La plataforma contará con múltiples niveles de acceso, asegurando que cada usuario
tenga funcionalidades específicas según su rol. Los usuarios tendrán la capacidad de
escribir y editar reseñas. Los administradores del sitio tendrán acceso completo

## Vista de inicio
Vista de inicio, para ususarios que no han iniciado sesión solo está disponible el acceso a Home (contiene el listado de libros) y Contacto
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/9ca940c5-fd6f-4f90-868f-b59841ccb100)

## Home
Vista Home muestra el listado de libros existentes con su nombre, autor e imagen
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/627f5c6d-f689-4cc7-953a-81f0f8410fa1)

## Contacto
Vista Contacto que contiene un formulario de contacto 
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/4ac0e335-9d28-4f56-9ade-2a0ca8790617)

## Inicio de sesión

![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/1ba2d799-a615-44cd-93e6-f7e28d35bd6a)

## Registarse
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/59d7e0f7-2a34-4bd8-ae5b-0310fc792887)

## /libro
Vista a la que se redirige al usuario una vez inicia sesión (En este caso ingresamos con un usuario no administrador), podemos ver el listado de libros y filtrar por diversas categorias, a diferencia de la vista anterior, podemos clickear tanto el titulo como el autor
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/8f9ca432-0cf8-4817-9732-2eedadcae5e5)

## libro/id/resenas
Al clickear el titulo de algun libro disponible, podemos ver informacion sobre el libro correspondiente y reseñas de otros usuarios, además podemos agregar reseñas
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/0bdb1195-c5c0-499f-88ce-963c27d5044c)

## /autor/id
Al clickear el autor en la vista anterior, seremos redirigidos a una pagina en donde podremos ver todas las obras del autor y comenzar a seguirlo
En este caso, ya seguimos al usuario por lo que el boton nos dirá dejar de seguir

![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/ccc4f6f1-9676-4410-97a2-e93a5f81f0fc)


## libro/nuevo/
Al logear con cuenta administradora, en el navbar aparece seccion crear libros
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/0b77f83c-3f3f-48d1-92e2-292b4a8d68de)

## Menu desplegable 
Al clickear nuestro nombre de usuario en el navbar, se despolegará un menu que permitirá cerrar sesión, ver reseñas hechas por el usuario y ver los autores seguidos
A modo de demostración, se muestra la sección de mis reseñas con el menu anteriormente desplegado
![image](https://github.com/Dolavarria/Proyecto_certificacion/assets/152653556/7de91c84-6c1a-44e1-97d7-66db5cc3e488)









## Prerrequisitos o Dependencias


- Este proyecto ha sido ejecutado correctamente en Windows 10 y 11
- Lenguaje de programación: Python 3.12.3
- Framework: Django 5.0.6
- Base de datos: PostgreSQL 16.2, 64-bit
- Librerias de Python:
  asgiref==3.8.1
  psycopg2==2.9.9
  sqlparse==0.5.0
  tzdata==2024.1

## Instalación del Proyecto

Instalar librerias necesarias contenidas en Requeriments.txt

```bash
pip install requeriments.txt
```

Una vez instalado,  crearemos una base de datos llamada resenas_libros en PostgreSQL, luego de esto podemos proceder a realizar las migraciones

```bash
py manage.py makemigrations
```
Aplicamos las migraciones

```bash
py manage.py migrate
```
Agregamos un usuario Lector y otro Administrador
```bash
py manage.py create_users
```
Agregamos datos semilla para Autores,Generos y Libros
```bash
py manage.py loaddata autor_generos_libros.json
```
Agregamos datos semilla para Reseñas
```bash
py manage.py loaddata resenas.json
```

Ejecutamos el proyecto
```bash
py manage.py runserver
```

## Credenciales de Acceso

### Para Usuario Tipo Administrador

- Usuario: Administrador
- Contraseña: Abc123#

### Para Usuario Tipo Huésped

- Usuario: Lector
- Contraseña: Abc123#

## Autor

- [Diego Olavarria](https://github.com/Dolavarria)
