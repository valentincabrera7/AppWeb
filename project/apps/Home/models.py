from django.db import models

class ProductoCategoria(models.Model):
    """CATEGORIAS DE PRODUCTOS"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria de Productos"
        verbose_name_plural = "Categorias de Productos"
