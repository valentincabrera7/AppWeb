from django.contrib import admin
from . import models

admin.site.register(models.Estudiante)
admin.site.register(models.Profesor)
admin.site.register(models.Curso)
