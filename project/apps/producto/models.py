from django.db import models


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre


