## AppWeb con Django ## (CREAR CARPETA)

# 1 Crear entorno virtual: python -m venv .venv

# 2 Activar entorno virtual: .venv/Scripts/Activate.ps1

# 3 mkdir project

# 4 Instalar Django: pip install django

# 5 Crear archivo .gitignore:
# .venv
# !**/migrations/__init__.py
# **/migrations/*.py
# __pycache__/

# 6 Crear archivo README.md y requirements.txt (este ultimo desde la consola)

# 7 git init para inicializar un repositorio vacio

# 8 django-admin startproject config . (Para crear la estructura de configuración de un proyecto Django, tener en cuenta el .) 

# 9 Crear views.py dentro de config

# 10 python manage.py startapp APP(nombre de la aplicación)

# 11 Registrar la app en config - settings.py

# 12 Despúes de crear modelos (clases) migrar para la base de datos
# python manage.py check app (para verificar posibles errores)
# python manage.py makemigrations (para que primeramente haga un seguimiento)
# python manage.py migrate (para que migre los modelos a la base de datos)
# python manage.py createsuperuser (para entrar al panel de administración de Django)

# 13 Registrar los modelos en admin.py

# 14 pip install djhtml

# 15 from django.core.management.utils import get_random_secret_key (clave aleatoria para el proyecto)