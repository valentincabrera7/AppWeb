from django.contrib import admin
from . import models #! Importación de la clase models.py (PARA LOS MODELOS)

admin.site.register(models.Pais)
admin.site.register(models.Cliente)

